# class MyException(Exception):
#     pass
#
# raise MyException("sndvopindvpin")

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
while True:
    try:
        x = int(input())
        print(1 / x)
    except ArithmeticError:
        print("do not divide by zero!!!")
    except ValueError:
        print("enter a number!!!")
    else:
        break

# else:
#     print("all is good")
# finally:
#     print("done")
