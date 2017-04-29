from unittest.mock import patch
import sys


class TestCountUpUsingWith:
    def test_count_up_decorator(self):
        # すでにimportされていることを考慮し、
        # そのtargetモジュールを無効化するためにsys.modulesより削除する
        # 未importの場合に例外KeyErrorとならないよう、第二引数にNoneを渡しておく
        sys.modules.pop('target', None)

        # 再度importしてパッチ
        with patch('deco.my_decorator.countup', lambda function: function):
            from target import Target

        # 検証
        sut = Target()
        actual = sut.execute_count_up()
        assert actual == 0

        # 使い終わったのでimportを削除
        sys.modules.pop('target')


class TestCountUpUsingStartStop:
    def test_count_up_decorator(self):
        sys.modules.pop('target', None)

        patcher = patch('deco.my_decorator.countup', lambda function: function)
        patcher.start()
        from target import Target
        patcher.stop()

        sut = Target()
        actual = sut.execute_count_up()
        assert actual == 0

        sys.modules.pop('target')


class TestCountUpUsingStartStopAll:
    def test_count_up_decorator(self):
        sys.modules.pop('target', None)

        patcher = patch('deco.my_decorator.countup', lambda function: function)
        patcher.start()
        from target import Target
        patch.stopall()

        sut = Target()
        actual = sut.execute_count_up()
        assert actual == 0

        sys.modules.pop('target')