from gendiff.differ import generate_diff
from tests import FIXTURE_PATH
import pytest


def generate_path(path):
    return f'{FIXTURE_PATH}{path}'


@pytest.mark.parametrize('file1, file2, format_name, result', [
    ('file1.json', 'file2.json', 'stylish', 'result_stylish_flat'),
    ('file1.yaml', 'file2.yml', 'stylish', 'result_stylish_flat'),
    ('file1_nested.json', 'file2_nested.json', 'stylish', 'result_stylish_nested'),
    ('file1_nested.json', 'file2_nested.json', 'plain', 'result_plain_nested'),
    ('file1_nested.json', 'file2_nested.json', 'json', 'result_json_nested'),
    ('file1.yaml', 'file2.yml', 'plain', 'result_plain_flat'),
    ('file1.json', 'file2.json', 'json', 'result_json_flat')
])
def test_gendiff(file1, file2, format_name, result):
    file1_path = generate_path(file1)
    file2_path = generate_path(file2)
    result_path = generate_path(result)
    with open(result_path) as file:
        expected = file.read()
        assert generate_diff(file1_path, file2_path, format_name) == expected
