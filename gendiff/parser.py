import json
import yaml


def parse(file, format_):
    if format_ == 'json':
        return json.loads(file)
    elif format_ == 'yaml':
        return yaml.safe_load(file)


def get_content(file_path):
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        data = open(file_path)
        return data.read(), 'yaml'
    elif file_path.endswith('.json'):
        data = open(file_path)
        return data.read(), 'json'
    raise Exception('Invalid file format.')
