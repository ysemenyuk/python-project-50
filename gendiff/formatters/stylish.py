signs = {
    'added': '+',
    'added': '+',
    'deleted': '-',
    'unchanged': ' ',
    'nested': ' ',
}


def make_indent(multiplier):
    return ' ' * multiplier


def make_output(lines, multiplier):
    result = "\n".join(lines)
    return f'{{\n{result}\n{make_indent(multiplier)}}}'


def stringify(value, multiplier, indent):
    if isinstance(value, dict):
        next_multiplier = multiplier + indent
        ind = make_indent(multiplier)
        lines = []
        for (name, value) in value.items():
            val = stringify(value, next_multiplier, indent)
            lines.append(f'{ind}    {name}: {val}')
        return make_output(lines, multiplier)
    elif value is None:
        return 'null'
    elif value is False:
        return 'false'
    elif value is True:
        return 'true'
    return value


def stylish_formatter(ast, multiplier=0, indent=4):
    next_multiplier = multiplier + indent
    ind = make_indent(multiplier)
    lines = []
    for node in ast:
        status = node.get('status')
        name = node.get("name")
        sign = signs.get(status)
        if status == 'nested':
            val = stylish_formatter(node.get("children"),
                                    next_multiplier, indent)
            lines.append(f'{ind}  {sign} {name}: {val}')
        elif node.get('status') == 'changed':
            del_sign = signs.get("deleted")
            add_sign = signs.get("added")

            old_val = stringify(node.get("old_value"), next_multiplier, indent)
            new_val = stringify(node.get("new_value"), next_multiplier, indent)

            lines.append(f'{ind}  {del_sign} {name}: {old_val}')
            lines.append(f'{ind}  {add_sign} {name}: {new_val}')
        else:
            val = stringify(node.get("value"), next_multiplier, indent)
            lines.append(f'{ind}  {sign} {name}: {val}')

    return make_output(lines, multiplier)
