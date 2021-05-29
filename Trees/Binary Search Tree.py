class Node():
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 

class BinarySearchTree():
    def __init__(self):
        self.root = None 
    
    def insert(self, value):
        new_node = Node(value)

        # If there is no root,
        if self.root == None:

            # Make the new node as the root
            self.root = new_node 
            return 
        else:
            # Initialize the current node
            current = self.root 

            while True:
                
                # If the new node <= current node
                if value < current.value:

                    # If the current node doesn't have a left node
                    if current.left == None:

                        # Assign the new node to the left
                        current.left = new_node
                        return 
                    else:
                        # Continue traversing down the tree as we assign the next left as the current node.
                        current = current.left 
                
                # If the new node > current node
                elif value > current.value:

                    # If the current value doesn't have a right value,
                    if current.right == None:

                        # Assign the new node as the right node
                        current.right = new_node
                        return  
                    else:

                        # Continue traversing down the tree as we assign the next right as the current node
                        current = current.right 


    def lookup(self, value):
        current = self.root 

        while True:

            # If the current node is null,
            if current == None:

                # return false
                return False 
            
            # If the given value == current value,
            if value == current.value:

                # return true
                return True 
           
            # If the current value <= given value,
            elif current.value <= value:

                # Continuing traversing the BST as we assign the current's left as the current value
                current = current.left 
            
            # If the current value > value,
            else:

                # Continuing travrsing the BST as we assign the current's right as the current value
                current = current.right 
        

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)

x = BinarySearchTree()
x.insert(10)
x.insert(5)
x.insert(6)
x.insert(12)
x.insert(8)
y = x.lookup(6)
print(y)