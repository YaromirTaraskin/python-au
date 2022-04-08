class ComplexExpression:
    def __init__(self, operation, *args):
        self.operation = operation
        self.args = args

    def unzip_postfix(self):
        return self.args[0], self.args[1], self.operation


my_operators = ["&", "|", "^", "**", "*", "/", "div", "mod", "//", "+", "-"]


def is_my_operator(s):
    return s in my_operators


def is_number_or_expression(s):
    return (not is_my_operator(s)) and ((type(s) == str and s.isnumeric) or type(s) == ComplexExpression)


def str_to_symbols(s: str):
    return s.split()


def solve(symbols):
    while len(symbols) >= 3:
        i = 0
        while i < len(symbols) - 2:
            if is_my_operator(symbols[i]) and is_number_or_expression(symbols[i + 1]) \
                    and is_number_or_expression(symbols[i + 2]):
                new_symbols = list(symbols[:i])
                new_symbols.append(ComplexExpression(*symbols[i:i + 3]))
                new_symbols.extend(symbols[i + 3:])
                symbols = new_symbols
            i += 1

    while True:
        if not any(map(lambda obj: type(obj) == ComplexExpression, symbols)):
            break
        i = 0
        while i < len(symbols):
            if type(symbols[i]) == ComplexExpression:
                new_symbols = symbols[:i]
                new_symbols.extend((symbols[i].unzip_postfix()))
                new_symbols.extend(symbols[i + 1:])
                symbols = new_symbols
                i += 2
            i += 1

    return symbols
