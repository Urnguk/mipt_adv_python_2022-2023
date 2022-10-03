class A:
    x = 0


class B:
    x = 5


class C(A, B):
    pass


c = C()
print(c.x)
A.x = 1
print(c.x)

