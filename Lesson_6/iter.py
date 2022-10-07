class StackIterator:
    def __init__(self, stack):
        self._stack = stack
        self._index = len(stack) - 1

    def __next__(self):
        res = self._stack._collection[self._index]
        if self._index < 0:
            raise StopIteration
        self._index -= 1
        return res


class Stack:
    def __init__(self):
        self._collection = []
        self._len = 0

    def __len__(self):
        return self._len

    def append(self, value):
        self._collection.append(value)
        self._len += 1

    def pop(self):
        self._len -= 1
        return self._collection.pop()

    def __iter__(self):
        return StackIterator(self)


A = Stack()
A.append(5)
A.append(3)
A.append(7)
A.append(6)
A.pop()
for element in A:
    print(element)
