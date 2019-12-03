# python_mock-sample

　
# Tested environment
## Mac

- Mac OS X 10.11.6
- Python 3.6.1
- pytest 3.0.7

　
## Windows

tested only `e.g_mocking_module` sample

- Windows10 x64
- Python 3.5.2 32bit
- pytest 3.0.5

　
# Samples

- `e.g._mocking_module/`
  - replace disabled package to mock
- `e.g._get_mock_object/`
  - get mock object from another mock object
- `e.g._set_self_attr/`
  - sample: unittest.mock.object(autospect=True)
- `e.g._called_count/`
  - assert called count & called args using MagicMock
- `e.g._mocking_decorator`
  - patch decorator using unittest.mock.patch
- `e.g._patch_constant`
  - patch constant using unittest.mock.patch

　
# Related Blog (Written in Japanese)

- [Pythonのテストコードで、モジュールをモックに差し替える - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/12/24/002922)
- [Pythonで、MagicMockのreturn_valueを使って、モックから別のモックを返してみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/03/09/060000)
- [Pytnonで、unittest.mock.patch.objectのautospecとside_effectを使って、テスト対象の属性(self.attr)を更新する - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/03/17/062138)
- [Pythonで、モックに差し替えたメソッドが呼ばれた回数や呼ばれた時の引数を検証する - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/03/18/063454)
- [Pythonで、unittest.mock.patchを使ってデコレータを差し替える - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2017/04/30/081331)
- [Pythonで、unittest.mock.patchを使って定数を差し替える - メモ的な思考的な](https://thinkami.hatenablog.com/entry/2019/12/03/232046)