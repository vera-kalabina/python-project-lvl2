import json
import yaml
import os


def parse(content, format_name):
    if format_name == 'json':
        return json.loads(content)
    if format_name in ('yml', 'yaml'):
        return yaml.safe_load(content)
    raise Exception('Invalid file format. Try .json or .yaml(yml) instead.')


def get_content(file_path):
    _, extension = os.path.splitext(file_path)
    format_name = extension[1:]
    data = open(file_path)
    return parse(data.read(), format_name)
