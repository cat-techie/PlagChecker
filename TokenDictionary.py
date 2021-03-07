import keyword


class TokenDictionary:

    operationsToken = {
        'MOP': ['+', '-', '*', '/', '%', '**', '//'],
        'COP': ['==', '>', '<', '>=', '<=', '!=', '<>'],
        'AOP': ['=', '+=', '-=', '*=', '/=', '%=', '**=', '//='],
        'BOP': ['&', '|', '^', '<<', '>>', '~']
    }

    namesToken = {
        'CYCLE': ['for', 'while'],
        'COND': ['if', 'elif', 'else'],
        'TRANSIT': ['break', 'continue', 'return'],
        'LOP': ['and', 'or', 'not'],
        'OOP': ['in', 'is']
    }
