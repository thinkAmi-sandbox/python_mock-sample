from target import get_mode
from unittest.mock import patch


@patch('target.DEBUG', False)
def test_production():
    actual = get_mode()
    assert actual == 'プロダクション'


@patch('target.DEBUG', new=False)
def test_production_with_new_keyword():
    actual = get_mode()
    assert actual == 'プロダクション'


def test_patch_using_with():
    with patch('target.DEBUG', False) as p:
        actual1 = get_mode()
        assert actual1 == 'プロダクション'

    actual2 = get_mode()
    assert actual2 == 'デバッグ'