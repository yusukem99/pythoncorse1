
class NotAttempted(Exception):
    pass

class Incorrect(Exception):
    pass

class UserlandExceptionIncorrect(Incorrect):
    """Raised when a user's solution is incorrect because it raised an (unexpected)
    exception when called.
    """
    def __init__(self, exception, args):
        self.wrapped_exception = exception
        self.msg  = ("あなたの関数を引数 `{!r}` で呼び出したところ、"
                "Pythonが次の例外を発生させました... **`{}: {}`**").format(
                        args, exception.__class__.__name__, exception)
    def __str__(self):
        return self.msg

class Uncheckable(Exception):
    pass
