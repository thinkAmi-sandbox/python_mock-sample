from unittest.mock import patch

# 引数があるデコレータでは関数のネストが1段階深いため、パッチもネストする
with patch('deco.my_decorator.add', lambda decorator_arg: lambda function: function):
    from target import Target

class TestAdd:
    def test_add_decorator(self):
        sut = Target()
        actual = sut.execute_add()
        assert actual == 0