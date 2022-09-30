
try:
    print(b)
    a = 10 / 0
except ZeroDivisionError:
    print("There was a division by zero attempt")
except Exception:
    print("smth")

