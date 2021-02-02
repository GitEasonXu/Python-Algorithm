#主要讨论装饰器和偏函数的关系
# partial:预先给某个函数传部分参数，在后面的使用中只需要传剩下的参数
# partial类似于带有配置项的装饰器


def decorator(*args, **kwargs):
    configs = args
    k_configs = kwargs
    #内置装饰器
    def inner_dec(f):
        #包装函数
        def wrapper(*args, **kwargs):
            #do_something(config)
            newkeywords = k_configs.copy()
            newkeywords.update(kwargs)
            return f(*args, **newkeywords)
        return wrapper
    return inner_dec

@decorator(negtive=True)  #decorator(negtive=True)(f)
def add(*args, **kwargs):
    print("kwargs: ", kwargs)
    print("args: ", args)
    if "negtive" in kwargs and kwargs["negtive"]:
        return -sum(args)
    else:
        return sum(args)

result = add(1,2,3,4,a=1,b=2,c=3)
print(result)

def partial(f, *args, **kwargs):
    configs = args
    k_configs = kwargs
    def wrapper(*args, **kwargs):
        k_configs.update(kwargs)
        return f(*args, **k_configs)
    return wrapper

def add(*args, **kwargs):
    print("kwargs: ", kwargs)
    print("args: ", args)
    if "negtive" in kwargs and kwargs["negtive"]:
        return -sum(args)
    else:
        return sum(args)

part = partial(add, negtive=True)
result = part(1,2,3,4,5, a=1, b=2, c=3)
print(result)


# partial(function, config)(*args, **kwargs)
# decorator(function, config)(*args, **kwargs)
# 两者是不是一样的，那么partial偏函数能不能实现装饰器呢 答案是肯定的。
# 偏函数和装饰器从实现思路上比较相似，它们之间有什么具体区别和不同么？
