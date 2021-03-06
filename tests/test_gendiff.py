from gendiff.main_logic.differ import generate_diff
from gendiff.formatters.formats import STYLISH
import pytest


JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
RESULT_STYLISH_FLAT = 'tests/fixtures/result_stylish_flat'


def get_right_result(path_to_file):
    file = open(path_to_file, 'r')
    result = file.read()
    return result


@pytest.mark.parametrize('file1, file2, stylish, result', [
    (JSON1, JSON2, STYLISH, RESULT_STYLISH_FLAT)
])
def test_gendiff(file1, file2, format_name, answer):
    assert generate_diff(file1, file2, format_name) == get_right_result(answer)