def build_ast_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []

    print(333, data2)
    
    for key in keys:
        if key not in data1:
            # print('added:', key)
            diff.append({'name': key, 'status': 'added', 'value': data2.get(key)})
        elif key not in data2:
            # print('deleted:', key)
            diff.append({'name': key, 'status': 'deleted', 'value': data1.get(key)})
        elif isinstance(data1.get(key), dict) and isinstance(data2.get(key), dict):
            # print('nested:', key)
            children = build_ast_diff(data1.get(key), data2.get(key))
            diff.append({'name': key, 'status': 'nested', 'children': children})
        elif data1.get(key) != data2.get(key):
            print('changed:', key, 'old_value', data1.get(key), 'new_value', data2.get(key))
            diff.append({'name': key, 'status': 'changed', 'old_value': data1.get(key), 'new_value': data2.get(key)})
        else:
            # print('equal:', key)
            diff.append({'name': key, 'status': 'unchanged', 'value': data2.get(key)})
  
    return diff

