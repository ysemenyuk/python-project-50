from gendiff.formatters.stylish import stylish

def formatting(ast, formatter):
  if formatter == 'sylish':
    return stylish(ast)
  else:
    return stylish(ast)
