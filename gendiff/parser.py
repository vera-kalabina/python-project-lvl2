import json
import yaml


def parse(file, format_name):
    if format_name == 'json':
        return json.loads(file)
    elif format_name == 'yaml':
        return yaml.safe_load(file)


def get_content(file_path):
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        data = open(file_path)
        return parse(data.read(), 'yaml')
    elif file_path.endswith('.json'):
        data = open(file_path)
        return parse(data.read(), 'json')
