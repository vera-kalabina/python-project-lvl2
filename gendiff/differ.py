from gendiff.parser import get_content
from gendiff.formatters import format_diff


def build_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    removed_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in added_keys:
            result[key] = {
                'status': 'added',
                'value': value2
            }
        elif key in removed_keys:
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
    data1 = get_content(filepath1)
    data2 = get_content(filepath2)
    diff = build_diff(data1, data2)
    return format_diff(diff, formatter)
