from gendiff.main_logic.parser import parse
from gendiff.formatters.formats import format_diff


def get_diff(data1, data2):
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
            result[(status, key)] = get_diff(value1, value2)
        else:
            status = 'changed'
            result[(status, key)] = [value1, value2]
    return result


def generate_diff(filepath1, filepath2, formatter='stylish'):
    file1 = parse(filepath1)
    file2 = parse(filepath2)
    diff = get_diff(file1, file2)
    return format_diff(diff, formatter)
