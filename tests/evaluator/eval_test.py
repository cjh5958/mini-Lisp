import pytest

from core.evaluator import eval
from core.environment import standard_env

class Testeval:
    @pytest.mark.parametrize(
        ("exp", "answer"),
        [
            (1, 1),
            ("#t", True),
            (["+", 1, 2], 3),
            ([1], 1),
            (["#t"], True)
        ]
    )
    def test_eval(
        self,
        exp,
        answer
    ):
        env = standard_env()
        assert eval(exp, env) == answer