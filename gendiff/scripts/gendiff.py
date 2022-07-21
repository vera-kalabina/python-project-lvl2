#!/usr/bin/env python


from gendiff.cli import parse
from gendiff.main_logic.differ import generate_diff


def main():
    parser = parse()
    difference = generate_diff(
        parser.first_file,
        parser.second_file
    )
    print (difference)


if __name__ == '__main__':
    main()