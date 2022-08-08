import json
import yaml


def parse(file):
    if file.endswith('.json'):
        data = json.load(open(file))
        return data
    elif file.endswith('.yml') or file.endswith('.yaml'):
        data = yaml.safe_load(open(file))
        return data