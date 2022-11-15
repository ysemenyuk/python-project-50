INDENT = 4

signs = {
  'added': '+',
  'added': '+',
  'deleted': '-',
  'unchanged': ' ',
  'nested': ' ',
}

# def make_line(node, multiplier):
#   status = node.get("status")
#   if status == 'changed':
#     lines = [
#       f'{make_indent(multiplier)}  {signs.get("deleted")} {node.get("name")}: {stringify(node.get("old"), multiplier + INDENT)}',
#       f'{make_indent(multiplier)}  {signs.get("added")} {node.get("name")}: {stringify(node.get("new"), multiplier + INDENT)}'
#     ]
#     return '\n'.join(lines)
#   return f'{make_indent(multiplier)}  {signs.get(status)} {node.get("name")}: {stringify(node.get("value"), multiplier + INDENT)}'

def stringify(value, multiplier):
  if not isinstance(value, dict):
    return value
  lines = []
  for (key, value) in value.items():
    lines.append(f'{make_indent(multiplier)}    {key}: {stringify(value, multiplier + INDENT)}')
  return make_output(lines, multiplier)

def make_indent(multiplier):
  return ' ' * multiplier

def make_output(lines, multiplier):
  result = "\n".join(lines)
  return f'{{\n{result}\n{make_indent(multiplier)}}}'
  
# def flatten(lst):
#   res = []
#   for item in lst:
#     if isinstance(item, list):
#       res.extend(flatten(item))
#     else:
#       res.append(item)
#   return res


def stylish(ast, multiplier = 0):
  next_multiplier = multiplier + INDENT
  lines = []
  for node in ast:
    status = node.get('status')
    if status == 'nested':
      lines.append(f'{make_indent(multiplier)}  {signs.get(status)} {node.get("name")}: {stylish(node.get("children"), next_multiplier)}')
    elif node.get('status') == 'changed':
      lines.append(f'{make_indent(multiplier)}  {signs.get("deleted")} {node.get("name")}: {stringify(node.get("old_value"), next_multiplier)}')
      lines.append(f'{make_indent(multiplier)}  {signs.get("added")} {node.get("name")}: {stringify(node.get("new_value"), next_multiplier)}')
    else:
      lines.append(f'{make_indent(multiplier)}  {signs.get(status)} {node.get("name")}: {stringify(node.get("value"), next_multiplier)}')
      
  return make_output(lines, multiplier)
