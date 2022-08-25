import json
import yaml


def parse_json(file):
    return json.load(open(file))


def parse_yaml(file):
    return yaml.safe_load(open(file))


def parse(file):
    if file.endswith('.json'):
        return parse_json(file)
    elif file.endswith('.yml') or file.endswith('.yaml'):
        return parse_yaml(file)
    raise Exception('Invalid file format.')
