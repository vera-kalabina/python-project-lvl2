import json


def format(difference):
    result = {}
    for head, value in difference.items():
        status, key = head
        if status == 'changed':
            result[key] = {
                'status': status,
                'old value': value[0],
                'new_value': value[1]
            }
        elif status == 'nested':
            result[key] = {
                'status': status,
                'value': format(value)
            }
        else:
            result[key] = {
                'status': status,
                'value': value
            }
    return result


def format_json(data):
    return json.dumps(format(data), indent=2)
