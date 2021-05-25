class Stack():
    def __init__(self):
        self.array = []
        self.length = 0
    
    # Returns the value of the last element
    def peek(self):
        return self.array[self.length - 1]
    
    # Adds the element at the end of the array
    def push(self, value):
        self.array.append(value)
        self.length += 1
    
    # Removes the element at the end of the array
    def pop(self):
        del self.array[self.length - 1]
        self.length -= 1
    
    # Returns the object's data instances
    def __str__(self):
        return str(self.__dict__)

x = Stack()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
print(x)
print(x.peek())
x.pop()
x.pop()
print(x)