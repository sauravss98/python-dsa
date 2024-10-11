from Node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0

        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    
    def print_list(self):
        print("Linked List: ")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next