class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, x):
        self.stack.append(x)
        return self

    def top(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

stack = Stack()

print(len(stack))

stack.push(5).push(6)

print(stack.top())

print(len(stack))

print(stack.pop())

print(stack.top())
