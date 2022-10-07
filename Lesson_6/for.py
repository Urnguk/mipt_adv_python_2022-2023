A = [0, 1, 2, 3, 4]
# for element in A:
#     print(element)

iterator = iter(A)
# print(iterator)
while(True):
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break
