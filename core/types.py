"""
types.py: Defines basic type of tokens.
"""
from typing import Optional, Self, TypeAlias

from core.handler import InvalidSymbol, TypeError, ParameterError

############ Token type definitions ############
Symbol: TypeAlias = str
Number: TypeAlias = int

class Token:
    """
    Token class: Generic token type definition.

    :param token: Single token to become a valid type
    :type token: :obj: 'str'

    :return: Instance of Number or Symbol
    :rtype: :class: 'core.types.Number' or :class: 'core.types.Symbol'

    :raise InvalidSymbol: Raise a InvalidSymbol if it's a token with an invalid format

    Examples:

    1.
        token = '123'
        try:
            return Token(token)
        except TypeError as e:
            print(e)
            return None
        
        >> get 123

    2.
        token = 'abc'
        try:
            return Token(token)
        except TypeError as e:
            print(e)
            return None
        
        >> get "abc"

    3.
        token = '12a'
        try:
            return Token(token)
        except TypeError as e:
            print(e)
            return None
        
        >> get InvalidSymbol("Invalid token: 12a")
        
    """
    Number = Number
    Symbol = Symbol
    Subtree: TypeAlias = list

    def __new__(cls: type[Self], token: str) -> Number | Symbol:
        try:
            return Number(token)
        except ValueError:
            pass

        reserved_words = cls.reserved_words()
        if cls._is_valid_symbol(token, reserved_words):
            return Symbol(token)

        raise InvalidSymbol(f"{token} was not a valid symbol.")

    @staticmethod
    def reserved_words() -> dict:
        """ Generate a map of all reserved words paired with corresponding lambda functions. """
        return {
            # Special form
            "fun":          lambda params, body: ...,
            "if":           lambda condition, then_expr, else_expr: ...,
            "define":       lambda name, value: ...,
            # Multiple params form
            "+":            lambda *x: (_ for _ in ()).throw(TypeError("`+` operator expected some 'Number' but got other.")) if any(type(arg) is not Number for arg in x) else eval('+'.join(map(str, x))),
            "*":            lambda *x: (_ for _ in ()).throw(TypeError("`*` operator expected some 'Number' but got other.")) if any(type(arg) is not Number for arg in x) else eval('*'.join(map(str, x))),
            "=":            lambda *x: (_ for _ in ()).throw(TypeError("`=` operator expected some 'Number' but got other.")) if any(type(arg) is not Number for arg in x) else eval('=='.join(map(str, x))),
            "and":          lambda *x: (_ for _ in ()).throw(TypeError("`and` operator expected some 'Boolean' but got other.")) if any(type(arg) is not bool for arg in x) else all(x),
            "or":           lambda *x: (_ for _ in ()).throw(TypeError("`or` operator expected some 'Boolean' but got other.")) if any(type(arg) is not bool for arg in x) else any(x),
            # Two params form
            "-":            lambda x, y: (_ for _ in ()).throw(TypeError("`-` operator expected two 'Number' but got other.")) if not (type(x) is Number and type(y) is Number) else x - y,
            "/":            lambda x, y: (_ for _ in ()).throw(TypeError("`/` operator expected two 'Number' but got other.")) if not (type(x) is Number and type(y) is Number) else ((_ for _ in ()).throw(ParameterError(f"{x} devided by 0.")) if y==0 else int(x / y)),  # divided by zero error
            "mod":          lambda x, y: (_ for _ in ()).throw(TypeError("`mod` operator expected two 'Number' but got other.")) if not (type(x) is Number and type(y) is Number) else x % y,
            ">":            lambda x, y: (_ for _ in ()).throw(TypeError("`>` operator expected two 'Number' but got other.")) if not (type(x) is Number and type(y) is Number) else x > y,
            "<":            lambda x, y: (_ for _ in ()).throw(TypeError("`<` operator expected two 'Number' but got other.")) if not (type(x) is Number and type(y) is Number) else x < y,
            # Single param form
            "not":          lambda x: (_ for _ in ()).throw(TypeError("`not` operator expected a 'Boolean' but got other.")) if not type(x) is bool else not x,
            "print-num":    lambda x: (_ for _ in ()).throw(TypeError("`print-num` function expected a 'Number' but got other.")) if not type(x) is Number else print(x),
            "print-bool":   lambda x: (_ for _ in ()).throw(TypeError("`print-bool` function expected a 'Boolean' but got other.")) if not type(x) is bool else print("#t" if x else "#f"),
            # Constants
            "#t":           True,
            "#f":           False
        }

    @staticmethod
    def _is_valid_symbol(token: str, reserved_words: Optional[dict] = {}) -> bool:
        """ Check if a token is a valid symbol. """
        import re

        if token in reserved_words:
            return True

        symbol_pattern = r'^[a-zA-Z][a-zA-Z0-9\-]*$'
        return re.match(symbol_pattern, token) is not None