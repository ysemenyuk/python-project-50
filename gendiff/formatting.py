from gendiff.formatters.stylish import stylish_formatter
from gendiff.formatters.json import json_fomatter
from gendiff.formatters.plain import plain_formatter


def formatting(ast, formatter):
    if formatter == 'json':
        return json_fomatter(ast)
    if formatter == 'plain':
        return plain_formatter(ast)
    else:
        return stylish_formatter(ast)
