class Node():
    def __init__(self, value):
        self.value = value
        self.next = None 

class SinglyLinkedList():
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

            # The length of the SLL is now one
            self.length = 1
        
        # If the head of the linked list is not null 
        else:
            # Make the new node as the next tail
            self.tail.next = new_node

            # Assign the new node as the tail of the node  
            self.tail = new_node

            # Increment the length of the SLL
            self.length += 1
    
    # Adds the node at the head of the LL
    def prepend(self, value):
        # Create a new node
        new_node = Node(value)

        # Make the head as the next node of the linked list
        new_node.next = self.head

         # Make the new node as the head 
        self.head = new_node

        # Increment the length of the SLL
        self.length += 1

    # Inserts a node at the specified index
    def insert(self, index, value):
        # Creates a new node
        new_node = Node(value)

        # Counter is created to keep track of the indices
        counter = 0

        # Set trav1 as the head
        trav1 = self.head

        # If the given index >= length of the SLL,
        if index>=self.length:
            
            # Add the node at the end of the SLL and return the SLL
            self.append(value)
            return 
        
        # If the given index == 0,
        if index ==0:

            # Add the node at the head of the SLL and return the SLL
            self.prepend(value)
            return
        
        # While the counter < length of the SLL,
        while counter < self.length:
            
            # If counter == index - 1 (since index starts at 0),
            if counter == index - 1:
                
                # Set the new node as the previous node's "next"
                # Set the previous node's "next" as the new node's "next"
                trav1.next, new_node.next = new_node, trav1.next

                # Increment the length of SLL
                self.length += 1

                # Stop the loop since we added the node 
                break

            # If the counter != index - 1, set the next node as trav1
            # to traverse through the SLL
            trav1 = trav1.next 

            # Increment the counter
            counter += 1
    
    # Remove a node
    def remove(self, index):
        # Initialize counter to keep track of indices
        counter = 0
        # Set first node as trav1
        trav1 = self.head 
        # Set the second node as trav2
        trav2 = self.head.next 

        # While counter < len(SLL)
        while counter < self.length:
            # If the given index is equal to index - 1 (since index starts at 0)
            if counter == index - 1:
                # temp is the node that we're going to remove
                # Set trav2 as the node that is next to the node that is going to be removed
                temp, trav2 = trav1.next, trav1.next.next 

                # Make the node that is previous to the node that we're going to remove point to trav2
                trav1.next = trav2

                # Decrease the length of the SLL
                self.length -= 1 

                # Stop the loop
                break

            # If counter != index - 1, set trav1 as the next node  
            trav1 = trav1.next 
            # and set trav2 as the node next to trav1
            trav2 = trav1.next
            # Increment the counter to keep track of the indicies
            counter += 1 
    
    # Reverse the SLL
    def reverse(self):
        prev = None 
        self.tail = self.head 

        while self.head is not None:
            temp = self.head 
            self.head = self.head.next 
            temp.next = prev 
            prev = temp 
        self.head = temp
        


    # Prints the whole SLL
    def printl(self):
        temp = self.head
        while temp is not None:
            print(temp.value , end = ' ')
            temp = temp.next
        print()

if __name__ == "__main__":
   x = SinglyLinkedList()
   x.append(1)
   x.append(2)
   x.append(3)
   x.append(4)
   x.reverse()
   x.printl()




