# from...importするとpatch()の引数で指定するモジュール名に影響が出る
# 今回はその点には触れないため、importとしておく
# 参考：http://qiita.com/FGtatsuro/items/eb2b05ff56f3599a1248
import called_count_library

class Target(object):
    def target_method(self):
        """複雑な処理をするけど、戻り値を戻さないメソッド"""
        c = called_count_library.Complex()
        c.set_complex('ham')
        c.set_complex('spam')
        c.set_complex('egg')
        c.set_complex('egg')
        c.set_complex_dict('hoge', {'fuga': 'piyo', 'くだもの': 'りんご'})
        c.set_complex_with_keyword('foo', str_arg='bar', dict_arg={'baz': 'qux', 'quux': 'foobar'} )
