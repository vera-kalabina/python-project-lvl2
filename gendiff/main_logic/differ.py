from gendiff.main_logic.opener import open_
from gendiff.formatters.stylish import stringify

def get_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        value1 = data1.setdefault(key)
        value2 = data2.setdefault(key)
        if value1 == None and value2 != None:
            status = '+'
            result[(status, key)] = value2 
        elif value1 != None and value2 == None:
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


def generate_diff(filepath1, filepath2):
    file1 = open_(filepath1)
    file2 = open_(filepath2)
    return stringify(get_diff(file1, file2))
