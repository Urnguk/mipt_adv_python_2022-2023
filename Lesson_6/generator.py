# A = (int(x) for x in input().split())
# for i in A:
#     print(i)


def squares():
    res = 0
    while True:
        if res == 100:
            break
        yield res**2
        res += 1




for i in squares():
    print(i)
#    if i > 10000:
#        break
