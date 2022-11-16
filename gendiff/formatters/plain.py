import gendiff.constants as const


COMPLEX_VALUE = '[complex value]'

ADDED_MSG = "Property '{}' was added with value: {}"
DELETED_MSG = "Property '{}' was removed"
CHANGED_MSG = "Property '{}' was updated. From {} to {}"


def stringify(value):
    if isinstance(value, (list, dict, tuple)):
        return COMPLEX_VALUE
    if value is None:
        return const.NULL
    if value is False:
        return const.FALSE
    if value is True:
        return const.TRUE
    if isinstance(value, (int, float)):
        return f"{value}"
    return f"'{value}'"


# flake8: noqa: C901
def plain_formatter(ast):
    def iter(ast, path):
        lines = []

        for node in ast:
            status = node.get(const.STATUS)
            name = node.get(const.NAME)
            prop_name = '.'.join([*path, name])

            if status == const.NESTED:
                ast = node.get(const.CHILDREN)
                next_path = [*path, name]
                lines.extend(iter(ast, next_path))

            elif status == const.CHANGED:
                old_value = stringify(node.get(const.OLD_VALUE))
                new_value = stringify(node.get(const.NEW_VALUE))
                message = CHANGED_MSG.format(prop_name, old_value, new_value)
                lines.append(message)

            elif status == const.ADDED:
                value = stringify(node.get(const.VALUE))
                message = ADDED_MSG.format(prop_name, value)
                lines.append(message)

            elif status == const.DELETED:
                message = DELETED_MSG.format(prop_name)
                lines.append(message)

        return lines

    lines = iter(ast, [])
    return "\n".join(lines)
