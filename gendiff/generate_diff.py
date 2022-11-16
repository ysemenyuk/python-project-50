from gendiff.get_data import get_data
from gendiff.build_ast_diff import build_ast_diff
from gendiff.formatting import formatting
# import json
# import os


def generate_diff(file_1, file_2, formatter_name='stylish'):
    print('generate_diff', file_1, file_2, formatter_name)
    data1 = get_data(file_1)
    data2 = get_data(file_2)

    ast_diff = build_ast_diff(data1, data2)
    # print(ast_diff)

    # with open('expected_json.json', 'w') as f:
    #     json.dump(ast_diff, f)

    return formatting(ast_diff, formatter_name)
