import pytest
from unittest.mock import patch, MagicMock, call
from called_count import Target

class Test_Target(object):
    def test_valid(self):
        mock_lib = MagicMock()
        with patch('called_count_library.Complex', return_value=mock_lib):
            sut = Target()
            sut.target_method()

            # set_complex()が呼ばれたか
            assert mock_lib.set_complex.called is True

            # set_complex()が1回でも呼ばれたか
            mock_lib.set_complex.assert_called()
            # set_complex()を呼んだ回数
            assert mock_lib.set_complex.call_count == 4

            # set_complex()が引数を伴って呼ばれたか
            # assert_called_with()は最後の呼び出しの引数をチェックする
            # mock_lib.set_complex.assert_called_with('ham') #=> fail
            mock_lib.set_complex.assert_called_with('egg')
            # 特定の引数で呼ばれたかを調べるには、assert_any_call()を使う
            mock_lib.set_complex.assert_any_call('ham')
            mock_lib.set_complex.assert_any_call('spam')
            # 特定の順序で、特定の引数が呼ばれたか
            mock_lib.set_complex.assert_has_calls([call('ham'), call('spam'), call('egg'), call('egg')])
            # 同じ引数がある場合、片方を省略しても良い
            mock_lib.set_complex.assert_has_calls([call('ham'), call('spam'), call('egg')])
            # 順番は気にしないけど、どの引数でも呼ばれたか
            mock_lib.set_complex.assert_has_calls([call('spam'), call('egg'), call('ham')], any_order=True)
            
            # 呼ばれた時の引数を詳しく調べる
            # call_argsは、最後に呼ばれた時の引数を取得
            args, kwargs = mock_lib.set_complex.call_args
            assert args[0] == 'egg'
            assert kwargs == {}

            # call_args_listは、呼ばれた時の引数を順番に取得できる
            list_args = mock_lib.set_complex.call_args_list
            assert list_args == [call('ham'), call('spam'), call('egg'), call('egg')]
            # callの中身はアンパックで取得
            unpack_args, unpack_kwargs = list_args[0]
            assert unpack_args == ('ham', )
            assert unpack_kwargs == {}

            # set_complex_dict()が1回呼ばれたか
            mock_lib.set_complex_dict.assert_called_once()
            # set_complex_dict()を呼んだ回数
            assert mock_lib.set_complex_dict.call_count == 1
            # 特定の引数で1回だけ呼ばれたか
            mock_lib.set_complex_dict.assert_called_once_with('hoge', {'fuga': 'piyo', 'くだもの': 'りんご'})
            # call_argsの確認
            multi_args, multi_kwargs = mock_lib.set_complex_dict.call_args
            assert multi_args[0] == 'hoge'
            assert multi_args[1] == {'fuga': 'piyo', 'くだもの': 'りんご'}
            assert multi_kwargs == {}

            # call_argsで、kwargsが返ってくるパターンの確認
            exist_args, exist_kwargs = mock_lib.set_complex_with_keyword.call_args
            assert exist_args[0] == 'foo'
            assert exist_kwargs == {'str_arg': 'bar', 'dict_arg': {'baz': 'qux', 'quux': 'foobar'}}

            # uncall()は1回も呼ばれていないか
            mock_lib.uncall_method.assert_not_called()
