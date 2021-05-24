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
        # Initialize counter, a new node, and the head
        counter = 0
        new_node = Node(value)
        trav1 = self.head 

        # If the given index is 0
        if index == 0:

            # Add the node at the head
            self.prepend(value)
            return 

        # If the given index >= length,
        if index >= self.length:
            
            # Add the node at the tail 
            self.append(value)
        
        # While the counter < length
        while counter < self.length:

            # If the counter == index - 1 (since index starts at 0)
            if counter == index - 1:

                # The trav1's next node is placed as a holder
                holder = trav1.next

                # The new node is then added next to trav1
                trav1.next = new_node

                # The holder becomes new node's "next"
                new_node.next = holder 

                # trav1 becomes new node's "previous"
                new_node.prev = trav1

                # The new node becomes the holder's "previous"
                holder.prev = new_node 
                self.length += 1 
                break 
                
            # If counter != index - 1, continue traversing
            trav1 = trav1.next  
            counter += 1
    
    # Removes an element at a specified index
    def remove(self, index):
        # Initialize counter to keep track of indices
        counter = 0
        trav1 = self.head 

        while counter < self.length:
            if counter == index - 1:
               remove_node = trav1.next 
               holder = remove_node.next 
               trav1.next = holder 
               holder.prev = trav1 
               self.length -= 1
               break 
            trav1 = trav1.next 

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
    # x.printl()
    x.append(4)
    x.printl()
    x.append(5)
    x.printl()
    x.append(10)
    x.printl()
    x.prepend(8)
    x.printl()
    x.insert(4, 6)
    x.printl()
    x.remove(2)
    x.printl()
    

