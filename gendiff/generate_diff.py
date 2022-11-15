import json

def generate_diff(file1, file2):
    # print('generate_diff', file1, file2)
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))

    keys = sorted(set(f1) | set(f2))
    result = []
    tab = '  '

    for key in keys:
        if not key in f1:
            # print('added:', key)
            result.append(f'{tab}+ {key}: {f2.get(key)}')
        elif not key in f2:
            # print('deleted:', key)
            result.append(f'{tab}- {key}: {f1.get(key)}')
        elif f1.get(key) != f2.get(key):
            # print('changed:', key)
            result.append(f'{tab}- {key}: {f1.get(key)}')
            result.append(f'{tab}+ {key}: {f2.get(key)}')
        else:
            # print('equal:', key)
            result.append(f'{tab}  {key}: {f1.get(key)}')

    result_string = "\n".join(result)
    open_result = '{\n'
    close_result = '\n}'

    return f'{open_result}{result_string}{close_result}'
