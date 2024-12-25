
class InterpreterException(Exception):
    """ Generic interpreter exception. """

    def __init__(self, value: str = ''):
        self.value = value

    def __str__(self) -> str:
        return self.__class__.__doc__.strip() + ": " + self.value if self.value else self.__class__.__doc__.strip()
    
class ParserException(InterpreterException):
    """ Generic exception while parsing """

class UndefinedSymbol(InterpreterException):
    """ Undefined symbol """

class InvalidSymbol(InterpreterException):
    """ Invalid symbol """

class TypeError(InterpreterException):
    """ Type error """

class NotExpectedArgument(InterpreterException):
    """ Syntax error """

class ParameterError(InterpreterException):
    """ Parameter error """