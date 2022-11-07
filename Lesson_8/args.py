def foo(a, *args, **kwargs):
    print(a)
    print(args, type(args))
    print(kwargs, type(kwargs))


# foo()
# foo(3)
foo(3, 5, 7, c="abc", d=8)
# a= [3, 4, 5]
# a.sort(key=, reverse=True)

def func(x, y):
    print(x, y)


d = dict()
d["x"] = 3
d["y"] = 5

func(**d)
