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
    for key, body in difference.items():
        status = body.get('status')
        value = body.get('value')
        if status == 'nested':
            result[STATUS[status] + key] = format(value)
        elif status == 'changed':
            old_value = body.get('old_value')
            new_value = body.get('new_value')
            result[STATUS['removed'] + key] = convert_value(old_value)
            result[STATUS['added'] + key] = convert_value(new_value)
        else:
            result[STATUS[status] + key] = convert_value(value)
    return result


def convert_value(value_):
    if value_ is None or isinstance(value_, bool):
        return edit_names(value_)
    elif not isinstance(value_, dict):
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


def format_stylish(data):
    return to_string(format(data))
