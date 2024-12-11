""" standard library """
from typing import NoReturn, Optional

def repl(prompt: Optional[str] = '') -> NoReturn:
    result = ""
    
    while True:
        try:
            user_input:str = input(prompt).strip()
            result += user_input
        except EOFError as e:
            print(result)
            break

def entry_point(args: list[str] | None):
    """ Entry point of the program. """
    try:
        from core.config import PROMPT
        repl(PROMPT)
    except ImportError:
        repl()