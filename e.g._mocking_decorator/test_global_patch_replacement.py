from unittest.mock import patch
from functools import wraps

# ダミーのデコレータを用意
# patch前に定義しないとエラー
# NameError: name 'dummy_decorator' is not defined
def dummy_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result + 9
    return wrapper

# ダミーのデコレータに差し替える
with patch('deco.my_decorator.countdown', lambda function: dummy_decorator(function)), \
        patch('deco.my_decorator.add', 
              lambda decorator_arg: lambda function: dummy_decorator(function)):
    from target import Target

class TestPatchArgs:
    def test_count_down_decorator(self):
        sut = Target()
        actual = sut.execute_count_down()
        assert actual == 9

    def test_add(self):
        sut = Target()
        actual = sut.execute_add()
        assert actual == 9
