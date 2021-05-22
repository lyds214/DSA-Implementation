class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.prev = None 

class DoublyLinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None    
        self.length = 0
    
    # Add a node a the tail 
    def append(self, value):
        # Create a new node
        new_node = Node(value)

        # If head is null
        if self.head is None:
            # Set new node as the head
            self.head = new_node

            # Set the head as the tail 
            self.tail = self.head 

            # Increment length
            self.length += 1
        
        # If the head is not null
        if self.head is not None:
            # Set the new node as tail's "next"
            self.tail.next = new_node 

            # Set the new node as the tail
            self.tail = new_node 

            # Increment the length 
            self.length += 1

    # Adds the node at the head of the DLL
    def prepend(self, value):
        # Creates a new node 
        new_node = Node(value)

        # Sets the head of the node as the new node's "next"
        new_node.next = self.head

        # The new node becomes the head's "previous "
        self.head.prev = new_node 

        # A new node now becomes the head 
        self.head = new_node 
        self.length += 1
            
            
    # Insert a node at a specified index 
    def insert(self, index, value):
        counter = 0
        trav1 = self.head 

        
        
     # Prints the whole DLL
    def printl(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end = ' ')
            temp = temp.next
        print()

if __name__ == "__main__":
    x = DoublyLinkedList()
    x.append(3)
    x.append(4)
    x.append(5)
    x.append(10)
    x.prepend(8)
    x.printl()

