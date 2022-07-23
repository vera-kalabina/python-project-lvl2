from gendiff.main_logic.opener import open_
from gendiff.formatters.formats import format_diff


def get_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        value1 = data1.setdefault(key)
        value2 = data2.setdefault(key)
        if value1 is None and value2 is not None:
            status = '+'
            result[(status, key)] = value2
        elif value1 is not None and value2 is None:
            status = '-'
            result[(status, key)] = value1
        elif value1 == value2:
            status = ' '
            result[(status, key)] = value1
        else:
            status1 = '-'
            result[(status1, key)] = value1
            status2 = '+'
            result[(status2, key)] = value2
    return result


def generate_diff(filepath1, filepath2, formatter='stylish'):
    file1 = open_(filepath1)
    file2 = open_(filepath2)
    diff = get_diff(file1, file2)
    return format_diff(diff, formatter)
