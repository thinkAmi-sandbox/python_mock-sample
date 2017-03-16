import pytest
from unittest.mock import patch
from set_self_attr import Target


class Test_Target(object):
    def test_can_patch(self):
        def validate_mock(self):
            self.can_print = True

        with patch.object(Target, 'validate', autospec=True, side_effect=validate_mock):
            sut = Target()
            actual = sut.target_method()
            assert actual == 'OK'

    @pytest.mark.xfail
    def test_can_not_patch(self):
        def validate_mock(self):
            # self.can_printを更新したいけど、selfが取れない
            # 引数にselfを入れようとすると、以下のエラー
            # > ret_val = effect(*args, **kwargs)
            # E TypeError: validate_mock() missing 1 required positional argument: 'self'
            self.can_print = True

        with patch.object(Target, 'validate', side_effect=validate_mock):
            sut = Target()
            actual = sut.target_method()
            assert actual == 'OK'
