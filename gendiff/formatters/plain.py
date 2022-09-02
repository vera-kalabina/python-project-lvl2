from gendiff.formatters.edit_names import edit_names


def walk(difference, path=''):
    result = []
    if not isinstance(difference, dict):
        return str(difference)
    for head, value in difference.items():
        status, key = head
        key_path = path + key
        if status == 'added':
            value = to_str(value)
            result.append(
                f"Property '{key_path}' was added with value: {value}"
            )
        elif status == 'removed':
            result.append(f"Property '{key_path}' was removed")
        elif status == 'changed':
            old = to_str(value[0])
            new = to_str(value[1])
            result.append(
                f"Property '{key_path}' was updated. From {old} to {new}"
            )
        elif status == 'nested':
            result.extend(walk(value, key_path + '.'))
    return result


def to_str(value_):
    if isinstance(value_, bool) or value_ is None or isinstance(value_, int):
        new_value = edit_names(value_)
        return f"{new_value}"
    elif isinstance(value_, dict):
        return '[complex value]'
    else:
        return f"'{value_}'"


def format_plain(data):
    return "\n".join(walk(data))
