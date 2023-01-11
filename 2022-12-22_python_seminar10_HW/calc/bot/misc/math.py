def get_check_parentheses(expression_src: str) -> bool:
    """Return a check for the number of parentheses."""
    if expression_src.count('(') != expression_src.count(')'):
        return False
    else:
        return True


def get_parse(expression_src: str) -> list:
    """Return a list of parts of an expression."""
    expression_parse = expression_src.replace(' ', '').strip() \
        .replace('^', ' ^ ').replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ') \
        .replace('(', ' ( ').replace(')', ' ) ') \
        .split()
    if (expression_parse[0] == '-') and is_number(expression_parse[1]):
        expression_parse[0] += expression_parse[1]
        expression_parse.pop(1)
    return expression_parse


def is_number(value: str) -> bool:
    """Return string validation as a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_slice_by_parentheses(expression_parse: list) -> list:
    """Return the expression as a list after the calculations in parentheses by precedence."""
    open_parenthesis, close_parenthesis = None, None
    expression_slice = []
    for index, item in enumerate(expression_parse):
        if item == '(':
            open_parenthesis = index
        elif item == ')':
            close_parenthesis = index
        if (open_parenthesis is not None) and (close_parenthesis is not None):
            expression_slice.extend(expression_parse[:open_parenthesis])
            expression_slice.extend(get_calculate(expression_parse[open_parenthesis + 1:close_parenthesis]))
            expression_slice.extend(expression_parse[close_parenthesis + 1:])
            break
    return expression_slice


def get_calculate(expression_parse: list) -> list:
    """Return the expression as a list after performing the calculation."""
    while len(expression_parse) > 1:
        if '^' in expression_parse:
            for i in range(len(expression_parse)):
                if get_operation(expression_parse, i, '^'):
                    break
        elif '*' in expression_parse or '/' in expression_parse:
            for i in range(len(expression_parse)):
                if get_operation(expression_parse, i, '*'):
                    break
                if get_operation(expression_parse, i, '/'):
                    break
        elif '+' in expression_parse or '-' in expression_parse:
            for i in range(len(expression_parse)):
                if get_operation(expression_parse, i, '+'):
                    break
                if get_operation(expression_parse, i, '-'):
                    break
    return expression_parse


def get_expression_solution(expression_src: str) -> float:
    """Return the result of evaluating the expression."""
    expression_parse = get_parse(expression_src)
    while len(expression_parse) > 1:
        if ('(' in expression_parse) and (')' in expression_parse):
            expression_parse = get_slice_by_parentheses(expression_parse)
        else:
            expression_parse = get_calculate(expression_parse)
    expression_res = round(float(expression_parse[0]), 4)
    return expression_res


def get_operation(expression_parse: list, i: int, operator: str) -> bool:
    """Return the result of evaluating a binary expression."""
    if expression_parse[i] == operator:
        expression_parse[i - 1] = list_operation.get(operator)(expression_parse[i - 1], expression_parse[i + 1])
        expression_parse.pop(i)
        expression_parse.pop(i)
        return True
    return False


list_operation = {
    '^': lambda x, y: float(x) ** float(y),
    '*': lambda x, y: float(x) * float(y),
    '/': lambda x, y: float(x) / float(y) if float(y) != 0 else 'Division by zero is not allowed!',
    '+': lambda x, y: float(x) + float(y),
    '-': lambda x, y: float(x) - float(y)
}
