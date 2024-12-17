"""
parser.py: 
"""
from core.config import DEBUG_MODE
from core.types import Token

def parse(program: str):
    tokens = tokenize(program)
    
    if DEBUG_MODE:
        print("="*15 + " Start Parse Process " + "="*15)
        print("List of all tokens:", tokens)

    rtn = []
    while not len(tokens) == 0:
        rtn.append(read_from_tokens(tokens=tokens))

    return rtn

def tokenize(s: str) -> list[str]:
    """ Convert a string into a list of tokens. """
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens: list[str]) -> list[Token]:
    """ Read an expression from a sequence of tokens. """
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')

    token = tokens.pop(0)

    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token: str) -> Token | None:
    """
    atom: Atomic function ensures token's atomicity
    The idea of "atomic parameter" means that it's not a compound expression in Lisp.
    """
    try:
        return Token(token)
    except TypeError as e:
        if DEBUG_MODE:
            print(e)
        return None