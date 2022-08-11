from gendiff.formatters.edit_names import edit_names


def format(difference, path=''):
    result = []
    if not isinstance(difference, dict):
        return str(difference)
    for head, value in difference.items():
        status, key = head
        key_path = path + key
        if status == 'added':
            value = convert_value(value)
            result.append(
                f"Property '{key_path}' was added with value: {value}"
            )
        elif status == 'removed':
            result.append(f"Property '{key_path}' was removed")
        elif status == 'changed':
            old = convert_value(value[0])
            new = convert_value(value[1])
            result.append(
                f"Property '{key_path}' was updated. From {old} to {new}"
            )
        elif status == 'nested':
            result.extend(format(value, key_path + '.'))
    return result


def convert_value(value_):
    if isinstance(value_, bool) or value_ is None:
        return f"{value_}"
    elif isinstance(value_, dict):
        return '[complex value]'
    else:
        return f"'{value_}'"


def to_string(data):
    return "\n".join(data)


def format_plain(data):
    return edit_names(to_string(format(data)))
