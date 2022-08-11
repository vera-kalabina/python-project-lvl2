import argparse
from gendiff.formatters.formats import JSON, STYLISH, PLAIN


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default=STYLISH,
        choices=[JSON, PLAIN, STYLISH]
    )
    args = parser.parse_args()
    return args
