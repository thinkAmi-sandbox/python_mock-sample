from functools import wraps

def countup(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result + 1
    return wrapper


def countdown(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result - 1
    return wrapper


def add(decorator_arg):
    """デコレータadd(@addとして使う)と、デコレータの引数decorator_arg"""

    def decorate(function):
        """デコレート対象の関数を引数fuctionとして受け取る、関数"""

        @wraps(function)
        def wrapped(*args, **kwargs):
            """デコレート対象の関数の引数をargsやkwargsとして受け取る、関数"""
            # デコレート対象の関数を実行し、結果をresultに入れる
            result = function(*args, **kwargs)
            # resultに対し、デコレータの引数を加算して戻す
            return result + decorator_arg

        # decorate関数は、デコレート対象の関数をラップするwrapped関数を返す
        return wrapped

    # add関数は、decorate関数を返す
    return decorate


def calculate(*decorator_args, **decorator_kwargs):
    u""""""
    def decorate(function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            result = function(*args, **kwargs)
            # 可変長引数で与えられた数を合計する
            summary = sum(decorator_args)
            # キーワード可変長引数に減算指定がある場合は減算、それ以外は加算
            if decorator_kwargs.get('is_decrement'):
                return result - summary
            else:
                return result + summary
        return wrapped
    return decorate
