with open("Test.txt", mode="r+") as f:
    print(f)
    f.seek(0)
    f.write("cccc")
    # print(f.tell())
    # print(f.readline())
    # print(f.tell())
    # print(f.readline())
    # print(f.tell())
    # f.seek(4)
    # print(repr(f.read(1)))
    # for x in f:
    #     print(x, end="")
print()