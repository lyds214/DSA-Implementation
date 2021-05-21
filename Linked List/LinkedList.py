class Node():
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None 
    
    # Adds the node 
    def append(self, value): 
        # Create a new node
        new_node = Node(value)

        # If the head of the node is null
        if self.head is None:
            # Make the new node as the head
            self.head = new_node 
            
            # Make the head as the tail
            self.tail = self.head
            self.length = 1
        
        # If the head of the linked list is not null 
        else:
            # Make the new node as the next tail
            self.tail.next = new_node
            # Assign the new node as the tail of the node  
            self.tail = new_node
            self.length += 1
    
    # Adds the node at the head of the LL
    def prepend(self, value):
        # Create a new node
        new_node = Node(value)

        # Make the first node as the next node of the linked list
        new_node.next = self.head

         # Make the new node as the head 
        self.head = new_node
        self.length += 1

    # Inserts a node at the specified index
    def insert(self, index, value):
        new_node = Node(value)
        counter = 0
        current_node = self.head

        if index>=self.length:
            self.append(value)
            return 
        if index ==0:
            self.prepend(value)
            return
        
        while counter < self.length:
            if counter == index - 1:
                current_node.next, new_node.next = new_node, current_node.next
                self.length += 1
                break
            current_node = current_node.next 
            counter += 1

    def printl(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end = ' ')
            temp = temp.next

if __name__ == "__main__":
   x = LinkedList()
   x.append(3)
   x.append(4)
   x.append(10)
   x.append(34)
   x.prepend(1)
   x.prepend(45)
   x.insert(4, 32)
   x.printl()



