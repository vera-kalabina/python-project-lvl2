from gendiff.parser import get_content, parse
from gendiff.formatters.formats import format_diff


def build_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1 and key in data2:
            result[key] = {
                'status': 'added',
                'value': value2
            }
        elif key in data1 and key not in data2:
            result[key] = {
                'status': 'removed',
                'value': value1
            }
        elif data1[key] == data2[key]:
            result[key] = {
                'status': 'not changed',
                'value': value1
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'status': 'nested',
                'value': build_diff(value1, value2)
            }
        else:
            result[key] = {
                'status': 'changed',
                'old_value': value1,
                'new_value': value2
            }
    return result


def generate_diff(filepath1, filepath2, formatter='stylish'):
    file1, format1 = get_content(filepath1)
    file2, format2 = get_content(filepath2)
    data1 = parse(file1, format1)
    data2 = parse(file2, format2)
    diff = build_diff(data1, data2)
    return format_diff(diff, formatter)
