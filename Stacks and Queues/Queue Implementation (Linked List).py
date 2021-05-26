class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Queue():
    def __init__(self):
        self.first = None 
        self.last = None 
        self.length = 0
    
    def peek(self):
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node 
            self.last = self.first 
            self.length += 1
        
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None 
        if self.first == self.last:
            self.last = None 
        
        self.first = self.first.next 
        self.length -= 1
    
    def printl(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end = ' -> ')
            temp = temp.next
        print()

x = Queue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
print(x.peek())
x.dequeue()
x.dequeue()
x.printl()