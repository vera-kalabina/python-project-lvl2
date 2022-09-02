from gendiff.parser import get_content, parse
from gendiff.formatters.formats import format_diff


def build_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1 and key in data2:
            status = 'added'
            result[(status, key)] = value2
        elif key in data1 and key not in data2:
            status = 'removed'
            result[(status, key)] = value1
        elif data1[key] == data2[key]:
            status = 'not changed'
            result[(status, key)] = value1
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            status = 'nested'
            result[(status, key)] = build_diff(value1, value2)
        else:
            status = 'changed'
            result[(status, key)] = [value1, value2]
    return result


def generate_diff(filepath1, filepath2, formatter='stylish'):
    file1, format1 = get_content(filepath1)
    file2, format2 = get_content(filepath2)
    data1 = parse(file1, format1)
    data2 = parse(file2, format2)
    diff = build_diff(data1, data2)
    return format_diff(diff, formatter)
