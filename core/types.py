"""
types.py: Defines basic type of tokens and exceptions.
"""
from typing import Optional, Self, TypeAlias

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

    :raise TypeError: Raise a TypeError if it's a token with an invalid format

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
        
        >> get TypeError("Invalid token: 12a")
        
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

        raise TypeError(f"Invalid token: {token}")

    @staticmethod
    def reserved_words() -> dict:
        """ Generate a map of all reserved words paired with corresponding lambda functions. """
        return {
            # Special form
            "fun":          lambda params, body: ...,
            "if":           lambda condition, then_expr, else_expr: then_expr if condition else else_expr,
            "define":       lambda name, value: ...,    # unused
            # Multiple params form
            "+":            lambda *x: eval('+'.join(map(str, x))),
            "*":            lambda *x: eval('*'.join(map(str, x))),
            "=":            lambda *x: eval('=='.join(map(str, x))),
            "and":          lambda *x: all(x),
            "or":           lambda *x: any(x),
            # Two params form
            "-":            lambda x, y: x - y,
            "/":            lambda x, y: int(x / y) if y != 0 else float("inf"),  # divided by zero error
            "mod":          lambda x, y: x % y,
            ">":            lambda x, y: x > y,
            "<":            lambda x, y: x < y,
            # Single param form
            "not":          lambda x: not x,
            "print-num":    lambda x: print(x),
            "print-bool":   lambda x: print("#t") if x else print("#f"),
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
    

class Procedure: ...

############ Exception type definitions ############
class InterpreterException(Exception):
    """ Generic interpreter exception. """

    def __init__(self, value: str = ''):
        self.value = value

    def __str__(self) -> str:
        msg = self.__class__.__doc__ or ''
        if self.value:
            msg = msg.rstrip('.')
            if "'" in self.value:
                value = self.value
            else:
                value = repr(self.value)
            msg += f': {value}'
        return msg
    
class ParserException(InterpreterException):
    """ Generic exception while parsing. """

class EvaluatorException(InterpreterException):
    """ Exception while evaluating. """

class InvalidSyntax(EvaluatorException):
    """ Invalid syntax. """

class UndefinedSymbol(EvaluatorException):
    """ Undefined symbol. """