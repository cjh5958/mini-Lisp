import pytest

from core.environment import Env, standard_env

class TestEnv:

    def test_basic(self):
        env = Env()
        assert env == {}

        params = ('a', 'b', 'c', 'd')
        args = (1, 2, 3, 4)

        assert Env(params, args, Env()) == {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4
        }

        assert Env(outer=Env(params, args)) == {}
        assert Env(outer=Env(params, args)).find('a') == {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4
        }

    @pytest.mark.parametrize(
        ("var", "args", "ans"),
        [
            ('+', [1, 2], 3),
            ('-', [1, 2], -1),
            ('*', [1, 3], 3),
            ('/', [6, 2], 3),
            ('/', [8, 3], 2),
            ("mod", [7, 3], 1),
            ("mod", [10, 2], 0),
            ("mod", [-5, 2], 1),
            ('>', [100, 99], True),
            ('>', [100, 100], False),
            ('>', [100, 101], False),
            ('<', [100, 101], True),
            ('<', [100, 100], False),
            ('<', [100, 99], False),
            ('=', [100, 100], True),
            ('=', [100, 99], False),
            ("and", [True, True], True),
            ("or", [False, False], False),
            ("or", [True, False], True),
            ("not", [True], False),
            ("not", [False], True)
        ]
    )
    def test_standard_env(self, var, args, ans):
        std_env = standard_env()
        op, x, ans = var, args, ans
        assert std_env.find(op)[op](*x) == ans