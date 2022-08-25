from gendiff.differ import generate_diff
import pytest


FIXTURE_PATH = 'tests/fixtures/'


def get_path(name):
    return f'{FIXTURE_PATH}{name}'


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
    file1_path = get_path(file1)
    file2_path = get_path(file2)
    result_path = get_path(result)
    with open(result_path) as file:
        answer = file.read()
    assert generate_diff(file1_path, file2_path, format_name) == answer
