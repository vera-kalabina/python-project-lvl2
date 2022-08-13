from gendiff.main_logic.differ import generate_diff
from gendiff.formatters.formats import PLAIN, STYLISH, JSON
import pytest


JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
YAML1 = 'tests/fixtures/file1.yaml'
YML2 = 'tests/fixtures/file2.yml'
JSON1_NESTED = 'tests/fixtures/file1_nested.json'
JSON2_NESTED = 'tests/fixtures/file2_nested.json'
RESULT_STYLISH_FLAT = 'tests/fixtures/result_stylish_flat'
RESULT_STYLISH_NESTED = 'tests/fixtures/result_stylish_nested'
RESULT_PLAIN_NESTED = 'tests/fixtures/result_plain_nested'
RESULT_JSON_NESTED = 'tests/fixtures/result_json_nested'



def get_right_result(path_to_file):
    file = open(path_to_file, 'r')
    result = file.read()
    return result


@pytest.mark.parametrize('file1, file2, format_name, result', [
    (JSON1, JSON2, STYLISH, RESULT_STYLISH_FLAT),
    (YAML1, YML2, STYLISH, RESULT_STYLISH_FLAT),
    (JSON1_NESTED, JSON2_NESTED, STYLISH, RESULT_STYLISH_NESTED),
    (JSON1_NESTED, JSON2_NESTED, PLAIN, RESULT_PLAIN_NESTED),
    (JSON1_NESTED, JSON2_NESTED, JSON, RESULT_JSON_NESTED)
])
def test_gendiff(file1, file2, format_name, result):
    assert generate_diff(file1, file2, format_name) == get_right_result(result)