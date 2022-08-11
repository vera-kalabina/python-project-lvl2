from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
    elif formatter == 'plain':
        return format_plain(diff)
