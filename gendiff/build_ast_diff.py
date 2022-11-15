def build_ast_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
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

