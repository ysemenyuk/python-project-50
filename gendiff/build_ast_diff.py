def build_ast_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        if key not in data1:
            # print('added:', key)
            node = {
                'name': key,
                'status': 'added',
                'value': data2.get(key)
            }
            diff.append(node)

        elif key not in data2:
            # print('deleted:', key)
            node = {
                'name': key,
                'status': 'deleted',
                'value': data1.get(key)
            }
            diff.append(node)

        elif isinstance(data1.get(key), dict) and \
                isinstance(data2.get(key), dict):
            # print('nested:', key)
            children = build_ast_diff(data1.get(key), data2.get(key))
            node = {
                'name': key,
                'status': 'nested',
                'children': children
            }
            diff.append(node)

        elif data1.get(key) != data2.get(key):
            # print('changed:', key, 'old_value', data1.get(key))
            # print('changed:', key, 'new_value', data2.get(key))
            node = {
                'name': key,
                'status': 'changed',
                'old_value': data1.get(key),
                'new_value': data2.get(key)
            }
            diff.append(node)

        else:
            # print('equal:', key)
            node = {
                'name': key,
                'status': 'unchanged',
                'value': data2.get(key)
            }
            diff.append(node)

    return diff
