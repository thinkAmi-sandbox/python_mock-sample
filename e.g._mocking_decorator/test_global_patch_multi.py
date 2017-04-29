from unittest.mock import patch

# withを使ったパッチ
with patch('deco.my_decorator.countup', lambda function: function), \
        patch('deco.my_decorator.countdown', lambda function: function):
    from target import Target


class TestCountUp:
    def test_count_up_decorator(self):
        sut = Target()
        actual = sut.execute_count_up()
        assert actual == 0
    
    def test_count_down_decorator(self):
        sut = Target()
        actual = sut.execute_count_down()
        assert actual == 0