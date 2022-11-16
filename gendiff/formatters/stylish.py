import gendiff.constants as const


SPACES_COUNT = 4
LINE = '{}  {} {}: {}'

signs_map = {
    const.ADDED: '+',
    const.DELETED: '-',
    const.UNCHANGED: ' ',
    const.NESTED: ' ',
}


def make_indent(multiplier):
    return ' ' * multiplier


def make_output(lines, multiplier):
    result = "\n".join(lines)
    return f'{{\n{result}\n{make_indent(multiplier)}}}'


def stringify(value, multiplier):
    if isinstance(value, dict):
        indent = make_indent(multiplier)
        next_multiplier = multiplier + SPACES_COUNT
        lines = []
        for (name, value) in value.items():
            value = stringify(value, next_multiplier)
            sign = signs_map.get(const.UNCHANGED)
            lines.append(LINE.format(indent, sign, name, value))
        return make_output(lines, multiplier)
    elif value is None:
        return const.NULL
    elif value is False:
        return const.FALSE
    elif value is True:
        return const.TRUE
    return value


def stylish_formatter(ast):
    def iter(ast, multiplier):
        next_multiplier = multiplier + SPACES_COUNT
        indent = make_indent(multiplier)
        lines = []

        for node in ast:
            status = node.get(const.STATUS)
            name = node.get(const.NAME)
            sign = signs_map.get(status)

            if status == const.NESTED:
                value = iter(node.get(const.CHILDREN), next_multiplier)
                lines.append(LINE.format(indent, sign, name, value))

            elif status == const.CHANGED:
                del_sign = signs_map.get(const.DELETED)
                add_sign = signs_map.get(const.ADDED)

                old_val = stringify(node.get(const.OLD_VALUE), next_multiplier)
                new_val = stringify(node.get(const.NEW_VALUE), next_multiplier)

                lines.append(LINE.format(indent, del_sign, name, old_val))
                lines.append(LINE.format(indent, add_sign, name, new_val))

            else:
                value = stringify(node.get(const.VALUE), next_multiplier)
                lines.append(LINE.format(indent, sign, name, value))

        return make_output(lines, multiplier)

    return iter(ast, 0)
