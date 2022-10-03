class MyException(Exception):
    pass
x = 77
raise MyException("sndvopindvpin" + str(x) + "{0}ab{1}c".format(x, 0))

# def k():
#     raise ValueError
# def g():
#     try:
#         return k()
#     except ValueError:
#         print("Value error")
# def f():
#     return g()
# try:
#     f()
# except ZeroDivisionError:
#     print("division by zero")
# attempts = 0
# while True:
#     try:
#         x = int(input())
#         print(1 / x)
#     except ArithmeticError:
#         print("do not divide by zero!!!")
#     except ValueError:
#         print("enter a number!!!")
#     else:
#         break
#     finally:
#         attempts += 1
#         print(attempts, "attempt")

# print(a)

# print(3 + "a")

# else:
#     print("all is good")
# finally:
#     print("done")
#
# class A:
#     pass
# x = A()
# print(x.x)

