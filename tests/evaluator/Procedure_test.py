import pytest
import sys

from core.config import DEBUG_MODE
from core.environment import standard_env
from core.evaluator import Procedure, eval_all

class TestProcedure:
    @pytest.mark.parametrize(
        ("param", "body", "args", "answer"),
        [
            (["x", "y"], ["+", "x", "y"], [5, 8], 13),
            (["x", "y"], ["mod", "x", "y"], [8, 3], 2),
            (["x", "y"], ["mod", "x", "y"], [["*", 2, 3], ["+", 2, 3]], 1)
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
            (["x"], ["+", "x", 1], [5], 6),
            (["x"], ["mod", "x", 2], [8], 0),
            (["x"], ["mod", "x", 5], [["*", 2, 3]], 1)
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
            ([2], 2),
            (["#t"], True)
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

    @pytest.mark.parametrize(
        ("param", "body", "args", "answer"),
        [
            (["x"], ["print-num", "x"], [1], '1\n'),
            (["x"], ["print-bool", "x"], ["#t"], "#t\n"),
            (["x", "y"], ["print-num", ["+", "x", ["*", "y", "y"]]], [5,4], '21\n')
        ]
    )
    def test_stdout(
        self,
        param: list, 
        body: list, 
        args: list, 
        answer,
        capsys
    ):
        env = standard_env()
        proc = Procedure(param, body, env)
        args = eval_all(args, env)
        proc(*args)
        captured = capsys.readouterr()
        if not DEBUG_MODE:
            assert captured.out == answer

    @pytest.mark.parametrize(
        ("name", "param", "body", "args", "answer"),
        [
            ('fact', ['n'], ['if', ['<', 'n', 3], 'n', ['*', 'n', ['fact', ['-', 'n', 1]]]], [2], 2),
            ('fact', ['n'], ['if', ['<', 'n', 3], 'n', ['*', 'n', ['fact', ['-', 'n', 1]]]], [3], 6),
            ('fact', ['n'], ['if', ['<', 'n', 3], 'n', ['*', 'n', ['fact', ['-', 'n', 1]]]], [4], 24),
            ('fib', ['x'], ['if', ['<', 'x', 2], 'x', ['+', ['fib', ['-', 'x', 1]], ['fib', ['-', 'x', 2]]]], [1], 1),
            ('fib', ['x'], ['if', ['<', 'x', 2], 'x', ['+', ['fib', ['-', 'x', 1]], ['fib', ['-', 'x', 2]]]], [3], 2),
            ('fib', ['x'], ['if', ['<', 'x', 2], 'x', ['+', ['fib', ['-', 'x', 1]], ['fib', ['-', 'x', 2]]]], [5], 5)
        ]
    )
    def test_recursion(
        self,
        name: str,
        param: list, 
        body: list, 
        args: list, 
        answer
    ):
        env = standard_env()
        env[name] = proc = Procedure(param, body, env)
        args = eval_all(args, env)
        assert proc(*args) == answer
