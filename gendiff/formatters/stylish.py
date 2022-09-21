from itertools import chain


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
    if depth == 0:
        return '\n'.join(chain('{', result, '}'))
    return '\n'.join(result)


def to_str(node, depth):
    if node is None:
        return 'null'
    if isinstance(node, bool):
        return str(node).lower()
    if not isinstance(node, dict):
        return node
    result = ['{']
    tab = INDENT * depth
    end = f'{tab}}}'
    for key, value in node.items():
        prefix = f"{tab}{INDENT}{key}"
        if isinstance(value, dict):
            line = f'{prefix}: {to_str(value, depth+1)}'
            result.append(line)
        else:
            line = f'{prefix}: {to_str(value, depth)}'
            result.append(line)
    result.extend([end])
    return '\n'.join(result)


def format_stylish(data):
    return walk(data)
