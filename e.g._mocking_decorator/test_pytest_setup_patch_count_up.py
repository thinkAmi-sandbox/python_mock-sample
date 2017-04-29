from unittest.mock import patch
import sys


class TestCountUpUsingWith:
    # 必要に応じて、クラスレベルやモジュールレベルにしても良い
    def setup_method(self):
        sys.modules.pop('target', None)

    def teardown_method(self):
        sys.modules.pop('target')

    def test_count_up_decorator(self):
        with patch('deco.my_decorator.countup', lambda function: function):
            from target import Target

        sut = Target()
        actual = sut.execute_count_up()
        assert actual == 0