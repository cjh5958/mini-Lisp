
class InterpreterException(Exception):
    """ Generic interpreter exception. """

    def __init__(self, value: str = ''):
        self.value = value

    def __str__(self) -> str:
        return self.value
    
class ParserException(InterpreterException):
    """ Generic exception while parsing. """

class UndefinedSymbol(InterpreterException):
    """ Undefined symbol. """

class InvalidSymbol(InterpreterException):
    """ Invalid symbol. """

class TypeError(InterpreterException):
    """ Type error. """

class SyntaxError(InterpreterException):
    """ Syntax error. """