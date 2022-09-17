INDENT = '    '
STATUS_PREFIXES = {
    'added': '  + ',
    'removed': '  - ',
    'not changed': '    '
}


def walk(difference, depth=0):
    result = []
    tab = INDENT * depth
    for key, body in difference.items():
        status = body.get('status')
        value = body.get('value')
        if status == 'nested':
            output_key = (f'{tab}{INDENT}{key}: '
                          f'{{\n{walk(value, depth+1)}')
            output_value = f'{tab}{INDENT}}}'
            result.extend([output_key, output_value])
        elif status == 'changed':
            old_value = body.get('old_value')
            new_value = body.get('new_value')
            output_key = (f'{tab}{STATUS_PREFIXES["removed"]}{key}: '
                          f'{to_str(old_value, depth+1)}')
            output_value = (f'{tab}{STATUS_PREFIXES["added"]}{key}: '
                            f'{to_str(new_value, depth+1)}')
            result.extend([output_key, output_value])
        else:
            output_line = (f'{tab}{STATUS_PREFIXES[status]}{key}: '
                           f'{to_str(value, depth+1)}')
            result.append(output_line)
    return '\n'.join(result)


def to_str(value_, depth):
    if value_ is None:
        return 'null'
    elif isinstance(value_, bool):
        return str(value_).lower()
    elif not isinstance(value_, dict):
        return value_
    result = ['{']
    tab = INDENT * depth
    end = f'{tab}}}'
    for key, value in value_.items():
        if isinstance(value, dict):
            line = f'{tab}{INDENT}{key}: {to_str(value, depth+1)}'
            result.append(line)
        else:
            line = f'{tab}{INDENT}{key}: {to_str(value, depth)}'
            result.append(line)
    result.extend([end])
    return '\n'.join(result)


def format_stylish(data):
    final_output = [
        '{',
        walk(data, depth=0),
        '}',
    ]
    return '\n'.join(final_output)
