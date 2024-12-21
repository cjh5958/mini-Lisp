"""
Core module: Core of Mini-Lisp interpreter.
"""

############ Library import ############
from typing import NoReturn, Optional

############ Modules import ############
try:
    from core.config import DEBUG_MODE
except ImportError:
    DEBUG_MODE = False
from core.environment import standard_env
from core.evaluator import eval_all
from core.parser import parse

############ Entry point ############
def repl(prompt: Optional[str] = '') -> NoReturn:
    """ Read-Evaluate-Print-Loop """

    program = ""

    while True:
        try:
            user_input: str = input(prompt)
            program += user_input
        except EOFError as e:
            break

    ast = parse(program)

    if DEBUG_MODE:
        print("Tokens AST after parsing:", ast)
        print("="*12 + " Start Evaluating Process " + "="*13)

    global_env = standard_env()

    eval_all(ast, global_env)


def entry_point(args: Optional[list[str]] = None):
    """ Mini-LISP Interpreter Entry Point. """
    try:
        from core.config import PROMPT
        repl(PROMPT)
    except ImportError:
        repl()