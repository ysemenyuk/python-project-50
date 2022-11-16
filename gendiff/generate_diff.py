from gendiff.get_data import get_data
from gendiff.build_ast_diff import build_ast_diff
from gendiff.formatting import formatting


def generate_diff(file_1, file_2, formatter_name='stylish'):
    data1 = get_data(file_1)
    data2 = get_data(file_2)

    ast_diff = build_ast_diff(data1, data2)

    return formatting(ast_diff, formatter_name)
