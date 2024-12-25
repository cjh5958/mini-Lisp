"""
evaluator.py: Core part of the interpreter
"""
from core.config import DEBUG_MODE
from core.environment import Env
from core.handler import InterpreterException, NotExpectedArgument
from core.types import Token

class Procedure:
    """ 
    class Procedure: User defined callable sub-procedure object .

    :param params: Declarations of parameters
    :type params: 'list[core.types.Token]'

    :param body: Body of the procedure
    :type body: 'list[core.types.Token]'

    :param env: Initial environment of the procedure, also the outer of local variables
    :type env: 'core.environment.Env'

    """
    def __init__(
        self,
        params: list[Token],
        body: list[Token],
        env: Env
    ): self.params, self.body, self.env = params, body, env

    def __call__(
        self,
        *args
    ):
        env = Env(self.params, args, self.env)
        if DEBUG_MODE:
            print('-'*10 + " Procedure called " + '-'*10)
            print("Current environment:")
            print(env)
        result = eval_all(self.body, env)
        return result[len(result)-1]

def eval(exp, env: Env):
    """ Evaluating function to evaluate each expressions in recursive way. """
    if DEBUG_MODE:
        print('-'*50)
        print("Current processing expression:", exp)

    # Number
    if isinstance(exp, Token.Number):
        if DEBUG_MODE:
            print("Type: Number -> Value is", exp)
        return exp

    # Symbol
    elif isinstance(exp, Token.Symbol):
        try:
            value = env.find(exp)[exp]
            if DEBUG_MODE:
                print("Type: Symbol -> Value is", value)
            return value
        except InterpreterException as e:
            print(e)
            exit(-1)
        
    # Subtree (Actually processing a list)
    op = exp[0]
    rwords = Token.reserved_words()
    if DEBUG_MODE:
        print("Type: Subtree -> First operation is", op)

    try:
        v = rwords.get(op, None)
        if not v == None:
            # Special cases
            if op == "if":                              # (if cond then_exp else_exp)
                (_, condition, then_expr, else_expr) = exp
                cond = eval(condition, env)
                if DEBUG_MODE:
                    print(f"Result of {condition} is", cond)
                return eval(then_expr if cond else else_expr, env)
            
            elif op == "define":                        # (define var exp)
                (_, var_name, var_value) = exp
                if DEBUG_MODE:
                    print(f"Defining `{var_name}`...")
                env[var_name] = eval(var_value, env)
                if DEBUG_MODE:
                    print(f"Value of `{var_name}` is {env[var_name]}")

            elif op == "fun":                           # (fun (params...) body)
                (_, *params) = exp
                (params, *body) = params
                return Procedure(params, body, env)

            # 1 param cases
            elif op == "not":
                (_, exp1) = exp
                try:
                    return env.find(op)[op](eval(exp1, env))
                except InterpreterException as e:
                    print(e)
                    exit(-1)
            
            elif op in ["print-num", "print-bool"]:
                (_, exp1) = exp
                arg = eval(exp1, env)
                if DEBUG_MODE:
                    print(f"Result of {exp1} is", arg)
                try:
                    env.find(op)[op](arg)
                except InterpreterException as e:
                    print(e)
                    exit(-1)

            # 2 params cases
            elif op in ["-", "/", "mod", ">", "<"]:     # (op exp exp)     
                (_, *exps) = exp
                if DEBUG_MODE:
                    print("2 params need to be processed first:", exps)
                try:
                    if not len(exps) == 2:
                        raise NotExpectedArgument(f"Need 2 arguments, but got {len(exps)}.")
                    args = eval_all(exps, env)
                    return env.find(op)[op](*args)
                except InterpreterException as e:
                    print(e)
                    exit(-1)
            
            # multiple params cases
            elif op in ["+", "*", "=", "and", "or"]:    # (op exp exp...)
                (_, *exps) = exp
                if DEBUG_MODE:
                    print(f"{len(exps)} params need to be processed first:", exps)
                try:
                    if len(exps) < 2:
                        raise NotExpectedArgument(f"Need at least 2 arguments, but got {len(exps)}.")
                    exps = eval_all(exps, env)
                    return env.find(op)[op](*exps)
                except InterpreterException as e:
                    print(e)
                    exit(-1)
            
            # constants
            else:
                return env.find(op)[op]
        
        else:                                           # (exp args...) or (Number) or (Symbol)
            (_, *args) = exp
            if DEBUG_MODE:
                print(f"{len(args) if len(args)>0 else 'No'} params need to be processed first:", args)
            args = eval_all(args, env)
            try:
                proc = env.find(op)[op]
                if DEBUG_MODE:
                    print(f"Entrying procedure `{op}`:", proc)
                return proc(*args)
            except InterpreterException as e:
                if isinstance(op, Token.Number): return op
                print(e)
                exit(-1)
                
    except TypeError:                                   # ((lambda) args...) or exp[0] is a list like [['>', 'x', 'y']]
        if len(exp)==1:
            val = eval(op, env)
            if DEBUG_MODE:
                print(f"{op}'s value is {val}")
            return val
        else:
            (_, *args) = exp
            args = eval_all(args, env)
            return eval(op, env)(*args)
        
def eval_all(exps: list, env: Env) -> list:
    r = []
    for i in range(len(exps)):
        result = eval(exps[i], env)
        if DEBUG_MODE:
            print(f"Result of {exps[i]} is", result)
        r.append(result)
    return r