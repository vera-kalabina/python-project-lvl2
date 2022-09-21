def walk(difference, path=''):
    result = []
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
    if path == '':
        return '\n'.join(result)
    return result


def to_str(value_):
    if isinstance(value_, bool):
        return f"{str(value_).lower()}"
    if value_ is None:
        return "null"
    if isinstance(value_, int):
        return f"{value_}"
    if isinstance(value_, dict):
        return '[complex value]'
    return f"'{value_}'"


def format_plain(data):
    return walk(data)
