f = open("test.txt", mode='r+')
print(f)
print(f.readline(), end="")
print(f.tell())
f.seek(0)
for line in f:
    print(line, end="")

f.close()
