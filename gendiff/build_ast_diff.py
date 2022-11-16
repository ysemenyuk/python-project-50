import gendiff.constants as const


def build_ast_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        if key not in data1:
            # print('added:', key)
            node = {
                const.NAME: key,
                const.STATUS: const.ADDED,
                const.VALUE: data2.get(key)
            }
            diff.append(node)

        elif key not in data2:
            # print('deleted:', key)
            node = {
                const.NAME: key,
                const.STATUS: const.DELETED,
                const.VALUE: data1.get(key)
            }
            diff.append(node)

        elif isinstance(data1.get(key), dict) and \
                isinstance(data2.get(key), dict):
            # print('nested:', key)
            children = build_ast_diff(data1.get(key), data2.get(key))
            node = {
                const.NAME: key,
                const.STATUS: const.NESTED,
                const.CHILDREN: children
            }
            diff.append(node)

        elif data1.get(key) != data2.get(key):
            # print('changed:', key, 'old_value', data1.get(key))
            # print('changed:', key, 'new_value', data2.get(key))
            node = {
                const.NAME: key,
                const.STATUS: const.CHANGED,
                const.OLD_VALUE: data1.get(key),
                const.NEW_VALUE: data2.get(key)
            }
            diff.append(node)

        else:
            # print('unchanged:', key)
            node = {
                const.NAME: key,
                const.STATUS: const.UNCHANGED,
                const.VALUE: data2.get(key)
            }
            diff.append(node)

    return diff
