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
            if current.value == value:

                # return true
                return True 
           
            # If the current value <= given value,
            elif value < current.value:

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
            print(str(curr_node.value))
            self.printt(curr_node.right)

    def BFSIterative(self):
        current_node = self.root 
        list = [] 
        queue = [] 

        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue[0]
            del queue[0]
            list.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        
        return list 
             

    def BFSRecursive(self, queue, list):
        if len(queue) == 0:
            return list 
        
        current_node = queue[0]
        del queue[0]
        list.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        
        if current_node.right:
            queue.append(current_node.right)
        
        return self.BFSRecursive(queue, list)
    
    def inOrder(self, current_node, list):
        if current_node != None:
            self.inOrder(current_node.left, list)
            list.append(current_node.value)
            self.inOrder(current_node.right, list)
        return list 
    
    def preOrder(self, current_node, list):
        if current_node != None:
            list.append(current_node.value)
            self.preOrder(current_node.left, list)
            self.preOrder(current_node.right, list)
        return list 
    
    def postOrder(self, current_node, list):
        if current_node.left:
            self.postOrder(current_node.left, list)
        if current_node.right:
            self.postOrder(current_node.right, list)
        list.append(current_node.value)
        return list



x = BinarySearchTree()
x.insert(10)
x.insert(5)
x.insert(6)
x.insert(12)
x.insert(8)
y = x.lookup(6)
print(y)
x.print_tree()
print(x.BFSIterative())
print(x.BFSRecursive([x.root], []))