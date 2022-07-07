def generate_diff(file1, file2):
    result = {}
    keys = sorted(file1.keys() | file2.keys())
    for key in keys:
        value1 = file1.setdefault(key)
        value2 = file2.setdefault(key)
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
            result[(status, key)] = value1
            status2 = '+'
            result[(status, key)] = value2
    return result


