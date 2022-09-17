import json
import yaml
import os


def parse(file, format_name):
    if format_name == 'json':
        return json.loads(file)
    elif format_name == 'yaml':
        return yaml.safe_load(file)


def get_content(file_path):
    split_name = os.path.splitext(file_path)
    format_name = split_name[-1]
    if format_name in ('.yml', '.yaml'):
        data = open(file_path)
        return parse(data.read(), 'yaml')
    elif format_name == '.json':
        data = open(file_path)
        return parse(data.read(), 'json')
    raise Exception('Invalid file format. Try .json or .yaml(yml) instead.')
