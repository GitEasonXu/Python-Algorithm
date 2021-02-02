import functools


class Demo(object):
    def __init__(self, str_value, *args) -> None:
        super(Demo, self).__init__()
        print("{} is {}".format(self.__class__.__name__, str_value))
        print("Args: ", args)


tf_export = functools.partial(Demo, "Hello!")
tf_export()
tf_export("World!", "Len")


def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    # newfunc.func = func
    # newfunc.args = args
    # newfunc.keywords = keywords
    return newfunc

def add(*args, **kwargs):
    print("args:", args)
    print("kwargs: ", kwargs)

func_part = partial(add, 1,2,a=1,b=2)
func_part(3,4,c=4)
# print(func_part.args)
