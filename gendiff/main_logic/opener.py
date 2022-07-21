import json


def open_(file):
    data = json.load(open(file))
    return data
