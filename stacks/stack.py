from node import Node
class Stack:
    def __init__(self,value=None):
        self.top = None
        self.length = 0
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.length = 1
    
    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.length -= 1
        return temp.value
    
    def peek(self):
        return self.top.value
    
    def print_stack(self):
        print("stack is: ")
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next