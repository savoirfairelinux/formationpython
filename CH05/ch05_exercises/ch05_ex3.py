class Stack:
    def __init__(self):
        self._lst = []

    def push(self, i):
        self._last = i
        self._lst += [i]

    def pop(self):
        del self._lst[-1]

    def top(self):
        return self._lst[-1]

    def __len__(self):
        return len(self._lst)

    def __bool__(self):
        return bool(self._lst)