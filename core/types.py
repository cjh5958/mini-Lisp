"""
types.py: Defines basic type of tokens.
"""
from typing import Optional, Self, TypeAlias

from core.handler import InvalidSymbol, TypeError, ParameterError, NotExpectedArgument

############ Token type definitions ############
Symbol: TypeAlias = str
Number: TypeAlias = int
Boolean: TypeAlias = bool

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
            "+":            lambda *x: eval('+'.join(map(str, x))) if TypeChecker('operator +', len(x), Number, *x) else ...,
            "*":            lambda *x: eval('*'.join(map(str, x))) if TypeChecker('operator *', len(x), Number, *x) else ...,
            "=":            lambda *x: eval('=='.join(map(str, x))) if TypeChecker('operator =', len(x), Number, *x) else ...,
            "and":          lambda *x: all(x) if TypeChecker('operator and', len(x), Boolean, *x) else ...,
            "or":           lambda *x: any(x) if TypeChecker('operator or', len(x), Boolean, *x) else ...,
            # Two params form
            "-":            lambda x, y: x - y if TypeChecker('operator -', 2, Number, x, y) else ...,
            "/":            lambda x, y: ((_ for _ in ()).throw(ParameterError(f"{x} devided by 0.")) if y==0 else int(x / y)) if TypeChecker('operator /', 2, Number, x, y) else ...,  # divided by zero error
            "mod":          lambda x, y: x % y if TypeChecker('operator mod', 2, Number, x, y) else ...,
            ">":            lambda x, y: x > y if TypeChecker('operator >', 2, Number, x, y) else ...,
            "<":            lambda x, y: x < y if TypeChecker('operator <', 2, Number, x, y) else ...,
            # Single param form
            "not":          lambda x: not x if TypeChecker('not', 1, Boolean, x) else ...,
            "print-num":    lambda x: print(x) if TypeChecker('print-num', 1, Number, x) else ...,
            "print-bool":   lambda x: print("#t" if x else "#f") if TypeChecker('print-bool', 1, Boolean, x) else ...,
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
    
def TypeChecker(function_name, count, type_name, *args) -> bool:
    for i in range(count):
        if not type(args[i]) == type_name:
            if callable(args[i]):
                raise NotExpectedArgument(f"Unexpected function called here ---> {args[i].params}.")
            raise TypeError(f"`{function_name}` expected {'some' if count > 2 else count} '{'Number' if type_name is Number else 'Boolean'}' but got other {'types' if count > 1 else 'type'}.")
    return True