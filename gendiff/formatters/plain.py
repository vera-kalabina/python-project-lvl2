def edit_names(diff):
    if diff is False:
        diff = "false"
    if diff is True:
        diff = "true"
    if diff is None:
        diff = "null"
    return diff


def walk(difference, path=''):
    result = []
    if not isinstance(difference, dict):
        return str(difference)
    for key, body in difference.items():
        status = body.get('status')
        value = body.get('value')
        key_path = path + key
        if status == 'added':
            value = to_str(value)
            result.append(
                f"Property '{key_path}' was added with value: {value}"
            )
        elif status == 'removed':
            result.append(f"Property '{key_path}' was removed")
        elif status == 'changed':
            old = to_str(body.get('old_value'))
            new = to_str(body.get('new_value'))
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
