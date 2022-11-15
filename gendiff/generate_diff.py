# import json
from gendiff.get_data import get_data

def generate_diff(file_1, file_2):
    # print('generate_diff', file1, file2)
    f1 = get_data(file_1)
    f2 = get_data(file_2)
    keys = sorted(set(f1) | set(f2))
    diff = []
    tab = '  '

    for key in keys:
        if key not in f1:
            # print('added:', key)
            diff.append(f'{tab}+ {key}: {f2.get(key)}')
        elif key not in f2:
            # print('deleted:', key)
            diff.append(f'{tab}- {key}: {f1.get(key)}')
        elif f1.get(key) != f2.get(key):
            # print('changed:', key)
            diff.append(f'{tab}- {key}: {f1.get(key)}')
            diff.append(f'{tab}+ {key}: {f2.get(key)}')
        else:
            # print('equal:', key)
            diff.append(f'{tab}  {key}: {f1.get(key)}')

    result = "\n".join(diff)
    open_result = '{\n'
    close_result = '\n}'

    return f'{open_result}{result}{close_result}'
