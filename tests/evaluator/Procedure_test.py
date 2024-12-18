import pytest

from core.environment import standard_env
from core.evaluator import Procedure, eval

class TestProcedure:

    @pytest.mark.parametrize(
        ("param", "body", "args", "answer"),
        [
            (["x"], ["+", "x", 1], [5], 6),
            (["x"], ["mod", "x", 2], [8], 0)
        ]
    )
    def test_1_param(
        self, 
        param: list, 
        body: list, 
        args: list, 
        answer
    ):
        env = standard_env()
        proc = Procedure(param, body, env)
        assert proc(args) == answer
