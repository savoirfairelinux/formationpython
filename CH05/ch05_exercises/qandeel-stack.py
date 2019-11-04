class BStack:
    def __init__(self):
        self.elements=[]

    def push(self,element):
        self.elements.append(element)

    def pop(self,element):
        if len(self.elements) != 0:
            element = self.elements[0]
            self.elements = self.elements[1:len(elements)-1]


    def __bool__(self):
        return (len(self.elements) == 0)

    def top(self):
        return self.elements(0)

    def __len__(self):
        return len(self.elements)

if __name__ == "__main__":
    myStack = BStack()
    myStack.push('A')
    myStack.push('B')
    myStack.push('C')
    print(len(myStack))
    print(bool(myStack))
    myStack.pop
    myStack.pop
    myStack.pop
    print(bool(myStack))