import time
from functools import lru_cache


def time_decorator(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper


@time_decorator
def odd(a):
    return a % 2


@time_decorator
def foo(x):
    for i in range(x):
        print(i)


@time_decorator
def my_summ(x, y, z):
    return x + y + z

# foo = time_decorator(foo)
# foo(10000)
# print(odd(3))
# print(my_summ(3, 4, 5))
# print(time.time())
# print(1/3)


# @time_decorator
@lru_cache(maxsize=None)
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@time_decorator
def Fib(n):
    return fib(n)


print(Fib(100))


