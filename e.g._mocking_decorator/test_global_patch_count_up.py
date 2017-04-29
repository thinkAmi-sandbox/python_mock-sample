from unittest.mock import patch

# withを使ったパッチ
# デコレータはimportした時に確定するため、importだけをwithの中に入れる
with patch('deco.my_decorator.countup', lambda function: function):
    from target import Target
    
# Mockオブジェクトのstart()とstopを使ったパッチ
# patcher = patch('deco.my_decorator.countup', lambda function: function)
# patcher.start()
# from target import Target
# patcher.stop()

class TestCountUp:
    def test_count_up_decorator(self):
        sut = Target()
        actual = sut.execute_count_up()
        assert actual == 0
