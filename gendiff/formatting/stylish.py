import itertools
from gendiff.formatting.get_description_value import get_description_value


def added_action(diff, result=None):
    if result is None:
        result = dict()
    for dict_ in diff:
        key = dict_['key']
        feature = dict_['type']
        match feature:
            case 'nested':
                result[key] = {}
                added_action(dict_['children'], result[key])
            case 'added':
                result.update({f"+ {key}": dict_['value']})
            case 'changed':
                result.update({f"- {key}": dict_['value']['before']})
                result.update({f"+ {key}": dict_['value']['after']})
            case 'unchanged':
                result.update({key: dict_['value']})
            case 'deleted':
                result.update({f"- {key}": dict_['value']})
    return result


def added_indent(value):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        replacer = ' '
        spaces_count = 4
        deep_indent_size = depth + spaces_count
        lines = []
        for key, val in current_value.items():
            if str(key)[0] in ['+', '-', ' ']:
                deep_indent = replacer * (deep_indent_size - 2)
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
            else:
                deep_indent = replacer * deep_indent_size
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')

        output = itertools.chain("{", lines, [replacer * depth + "}"])
        return '\n'.join(output)

    return iter_(value, 0)


def get_stylish_format(diff):
    dict_diff = added_action(diff)
    stylish_format = added_indent(dict_diff)
    return get_description_value(stylish_format)
