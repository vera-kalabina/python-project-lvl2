from gendiff.formatters.edit_names import edit_names


INDENT = '    '
STATUS = {
    'added': '  + ',
    'removed': '  - ',
    'not changed': '    ',
    'nested': '    '
}


def format(difference):
    result = {}
    if not isinstance(difference, dict):
        return str(difference)
    for head, value in difference.items():
        status, key = head
        if status == 'nested':
            result[STATUS[status] + key] = format(value)
        elif status == 'changed':
            result[STATUS['removed'] + key] = convert_value(value[0])
            result[STATUS['added'] + key] = convert_value(value[1])
        else:
            result[STATUS[status] + key] = convert_value(value)
    return result


def convert_value(value_):
    if not isinstance(value_, dict):
        return value_
    result = {}
    for key, value in value_.items():
        new_key = '    {}'.format(key)
        result[new_key] = convert_value(value)
    return result


def to_string(data, lvl=0):
    result = "{\n"
    for key, value in data.items():
        if isinstance(value, dict):
            value = to_string(value, lvl + 1)
        result += f'{INDENT * lvl}{key}: {value}\n'
    result += f'{INDENT * lvl}}}'
    return result


def format_json(data):
    return edit_names(to_string(format(data)))
