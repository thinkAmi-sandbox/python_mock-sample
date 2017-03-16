# mockを作るための標準ライブラリ
from unittest.mock import MagicMock
# テスト対象クラス
from get_mock_object import Target
# モックで差し替えるクラスが含まれるモジュール
import cook

def test_bake():
    # cuisine.Eggが返ってくると仮定したテストをしたい

    #------------
    # モックを準備
    # cuisineのモックを作る
    mock_cuisine = MagicMock()
    # get_name()メソッドは、'egg'を返すように指定
    mock_cuisine.get_name.return_value = 'egg'

    # bake()メソッドでcuisineのモックを返す、モックを作る
    mock_cook = MagicMock()
    # bake()メソッドは、上記で作ったモック'mock_cuisine'を返すように指定
    mock_cook.bake.return_value = mock_cuisine

    # Cookクラスはモックを返すモックに差し替える
    cook.Cook = mock_cook

    #------------
    # テスト実行
    sut = Target()
    # runの引数materialは、本来作るのが面倒
    # 今回はモック向けなので、何かあれば良いというレベル
    actual = sut.run('dummy')

    # eggが返ってくることを検証
    # bakeメソッドの中で例外が発生しない限り返ってこないはずが、
    # モックで差し替えているため、eggが返ってきている
    assert actual['cuisine'] == 'egg'
