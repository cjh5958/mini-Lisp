"""
evaluator.py: 
"""
from core.config import DEBUG_MODE
from core.environment import Env
from core.types import Token

class Procedure:
    """ 
    class Procedure: User defined callable sub-procedure object .

    :param params: 
    :type params: 'list[core.types.Token]'

    :param body:
    :type body: 'list[core.types.Token]'

    :param env:
    :type env: 'core.environment.Env'

    """
    def __init__(
        self,
        params: list[Token],
        body: list[Token],
        env: Env
    ): self.params, self.body, self.env = params, body, Env(outer=env)

    def __call__(
        self,
        args: list
    ):
        self.env.update(zip(self.params, args))
        return eval(self.body, self.env)


def eval(exp, env: Env):
    if DEBUG_MODE:
        print('-'*50)
        print("Current processing expression:", exp)

    # Number
    if isinstance(exp, Token.Number):
        if DEBUG_MODE:
            print("Type: Number -> Nothing to do.")
        return exp

    # Symbol
    elif isinstance(exp, Token.Symbol):
        value = env.find(exp)[exp]
        if DEBUG_MODE:
            print("Type: Symbol -> Value is", value)
        return value

    # Subtree(Actually processing a list)
    op = exp[0]
    rwords = Token.reserved_words()
    if DEBUG_MODE:
        print("Type: Subtree -> First operation is", op)

    if isinstance(op, Token.Subtree):               # ((fun (params...) body) args...)
        (_, *args) = exp
        return eval(op, env)(args)

    elif not rwords.get(op, None) == None:    # reserved words

        # Special cases
        if op == "if":                              # (if cond then_exp else_exp)
            (_, condition, then_expr, else_expr) = exp
            return eval(then_expr if eval(condition, env) else else_expr, env)
        
        elif op == "define":                        # (define var exp)
            (_, var_name, var_value) = exp
            env[var_name] = eval(var_value, env)

        elif op == "fun":                           # (fun (params...) body)
            (_, *params) = exp
            (params, body) = params
            return Procedure(params, body, env)

        # 1 param cases
        elif op == "not":
            (_, exp1) = exp
            return env.find(op)[op](eval(exp1, env))
        
        elif op in ["print-num", "print-bool"]:
            (_, exp1) = exp
            env.find(op)[op](eval(exp1, env))

        # 2 params cases
        elif op in ["-", "/", "mod", ">", "<"]:     # (op exp exp)     
            (_, exp1, exp2) = exp
            return env.find(op)[op](eval(exp1, env), eval(exp2, env))
        
        # multiple params cases
        elif op in ["+", "*", "=", "and", "or"]:    # (op exp exp+)
            (_, *exps) = exp
            eval_all(exps, env)
            return env.find(op)[op](*exps)
        
def eval_all(exps: list, env: Env):
    for i in range(len(exps)):
        exps[i] = eval(exps[i], env)