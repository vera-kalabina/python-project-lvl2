import itertools
from gendiff.formatters.edit_names import edit_names


def format_stylish(value, replacer=' ', spaces_count=1):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        depth_size = depth + spaces_count
        lines = []
        for key, val in current_value.items():
            replacer = f'  {key[0]} '
            deep_indent = replacer * depth_size
            current_indent = replacer * depth
            lines.append(f'{deep_indent}{key[1]}: {iter_(val, depth_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return edit_names('\n'.join(result))
    return iter_(value, 0)
