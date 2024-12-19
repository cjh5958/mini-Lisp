import json
from typing import Any, Callable, Optional, Self

from core.types import Token
from core.types import UndefinedSymbol

class Env(dict):
    """
    Env class: Core part of the interpreter to store the scope of variables or functions.
    An environment: A standard dict of {'var': val} pairs, with an outer Env.

    :param params: Construct the 'var' part of Env
    :type params: :obj: 'Literal[...]'

    :param args: Construct the 'val' part of Env
    :type args: :obj: 'Literal[...]'

    :param outer: Another Env outer itself
    :type outer: :obj: 'core.environment.Env'

    """
    def __init__(
            self,
            params = (),
            args = (),
            outer: Optional[Self] = None
        ):
        self.update(zip(params, args))
        self.outer = outer
    
    def to_dict(self) -> dict[str, Any]:
        r = {}
        for key, val in self.items():
            r[key] = "Procedure" if isinstance(val, Callable) else val
        if self.outer:
            r["outer"] = self.outer.to_dict()
        return r

    def __str__(self):
        """ Visualize Env structure for debugging. """
        formatted_dict = self.to_dict()
        return json.dumps(formatted_dict, indent=2, skipkeys=True)

    def find(self, var) -> Self | None:
        """
        Find the innermost Env layer where var appears.

        :param var: Target token to be found in Env
        :type var: :obj: 'core.types.Token'

        :return: Env which contains the target token innermost or None if not found
        :rtype: :dict: 'core.environment.Env'
        :rtype: None

        :raise Exception: :core.types.UndefinedSymbol:  Symbol name not defined in neither local nor global scope

        """
        if var in self: return self
        if self.outer is not None:
            return self.outer.find(var)
        raise UndefinedSymbol("Undefined symbol")

def standard_env() -> Env:
    """ The way to get a basic environment with some Scheme standard procedures. """
    env = Env()
    env.update(
        Token.reserved_words()
    )
    return env