class Array():
    def __init__(self):
        self.length = 0
        self.value = {} 
    
    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.value[index]
    
    def push(self, element):
        self.value[self.length] = element 
        self.length += 1 
    
    def pop(self):
        last_element = self.value[self.length - 1]
        del self.value[self.length - 1]
        self.length -= 1
        
        return last_element 
    
    def remove(self, index):
        delete_item = self.value[index]

        for x in range(index, self.length - 1):
            self.value[i] = self.value[i + 1]

        del self.value[self.length - 1]
        self.length -= 1

        return delete_item
