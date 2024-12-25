import pytest
import sys

from core.config import DEBUG_MODE
from core.environment import standard_env
from core.evaluator import Procedure, eval_all

class TestProcedure:
    @pytest.mark.parametrize(
        ("param", "body", "args", "answer"),
        [
            (["x", "y"], [["+", "x", "y"]], [5, 8], 13),
            (["x", "y"], [["mod", "x", "y"]], [8, 3], 2),
            (["x", "y"], [["mod", "x", "y"]], [["*", 2, 3], ["+", 2, 3]], 1)
        ]
    )
    def test_2_param(
        self, 
        param: list, 
        body: list, 
        args: list, 
        answer
    ):
        env = standard_env()
        proc = Procedure(param, body, env)
        args = eval_all(args, env)
        assert proc(*args) == answer

    @pytest.mark.parametrize(
        ("param", "body", "args", "answer"),
        [
            (["x"], [["+", "x", 1]], [5], 6),
            (["x"], [["mod", "x", 2]], [8], 0),
            (["x"], [["mod", "x", 5]], [["*", 2, 3]], 1)
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
        args = eval_all(args, env)
        assert proc(*args) == answer

    @pytest.mark.parametrize(
        ("body","answer"),
        [
            ([[2]], 2),
            ([["#t"]], True)
        ]
    )
    def test_0_param(
        self,
        body: list,
        answer
    ):
        env = standard_env()
        proc = Procedure([], body, env)
        assert proc() == answer
