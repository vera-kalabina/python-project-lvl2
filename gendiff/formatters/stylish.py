INDENT = '    '
STATUS = {
    'added': '  + ',
    'removed': '  - ',
    'not changed': '    ',
    'nested': '    '
}


def edit_names(diff):
    if diff is False:
        diff = "false"
    if diff is True:
        diff = "true"
    if diff is None:
        diff = "null"
    return diff


def walk(difference, lvl=0):
    if not isinstance(difference, dict):
        return str(difference)
    result = []
    tab = INDENT * lvl
    for key, body in difference.items():
        status = body.get('status')
        value = body.get('value')
        if status == 'nested':
            output_key = f'{tab}{INDENT}{key}: '\
                f'{{\n{walk(value, lvl+1)}'
            output_value = f'{tab}{INDENT}}}'
            result.extend([output_key, output_value])
        elif status == 'changed':
            old_value = body.get('old_value')
            new_value = body.get('new_value')
            output_key = f'{tab}  - {key}: '\
                f'{convert_value(old_value, lvl+1)}'
            output_value = f'{tab}  + {key}: '\
                f'{convert_value(new_value, lvl+1)}'
            result.extend([output_key, output_value])
        else:
            output_line = f'{tab}{STATUS[status]}{key}: '\
                f'{convert_value(value, lvl+1)}'
            result.append(output_line)
    return '\n'.join(result)


def convert_value(value_, depth):
    if value_ is None or isinstance(value_, bool):
        return edit_names(value_)
    elif isinstance(value_, dict):
        result = ['{']
        tab = INDENT * depth
        end = f'{tab}}}'
        for key, value in value_.items():
            if isinstance(value, dict):
                line = f'{tab}{INDENT}{key}: {convert_value(value, depth+1)}'
                result.append(line)
            else:
                line = f'{tab}{INDENT}{key}: {convert_value(value, depth)}'
                result.append(line)
        result.extend([end])
        return '\n'.join(result)
    else:
        return value_


def format_stylish(data):
    final_output = [
        '{',
        walk(data, lvl=0),
        '}',
    ]
    return '\n'.join(final_output)
