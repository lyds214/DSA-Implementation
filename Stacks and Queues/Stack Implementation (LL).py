class Node():
    def __init__(self, value):
        self.value = value
        self.next = None 
    
class Stack():
    def __init__(self):
        self.top = None 
        self.bottom = None 
        self.length = 0
    
    
    # Peek the top of the stack
    def peek(self):
        # return the top 
        return self.top.value
    
    # Adding the value to the stack
    def push(self, value):
        # Create a new node 
        new_node = Node(value)
        # Initialize a reference a variable
        temp = self.top 
        # ASsign the new node to the top of the stack 
        self.top = new_node 
        # Assign the reference variable next to the top of the stack 
        self.top.next = temp

        self.length += 1

    #  Removing the element from the top 
    def pop(self):

        # Initialize the top element to remove 
        remove_node = self.top 

        # Assign the next node as the head of the node 
        self.top = self.top.next
        self.length -= 1

    # Prints the whole LL
    def printl(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end = ' -> ')
            temp = temp.next
        print()


x = Stack() 
x.push("google")
x.push("microsoft")
x.push("Facebook")
x.push("apple")
x.pop()
x.pop()
x.printl()
        