from gendiff.get_data import get_data
from gendiff.build_ast_diff import build_ast_diff
from gendiff.formatting import formatting
import json

def generate_diff(file_1, file_2, formatter = 'stylish'):
    # print('generate_diff', file1, file2)
    data1 = get_data(file_1)
    data2 = get_data(file_2)

    ast = build_ast_diff(data1, data2)

    # print(data2)
    
    # with open('3.json', 'w') as f:
    #     json.dump(ast, f, indent=4)

    return formatting(ast, formatter)

    # result = "\n".join(diff)
    # open_result = '{\n'
    # close_result = '\n}'

    # return f'{open_result}{result}{close_result}'
