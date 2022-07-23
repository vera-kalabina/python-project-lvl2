from gendiff.formatters.stylish import format_stylish

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
