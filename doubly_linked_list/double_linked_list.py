from node import Node

class DoubleLinkedList:
    def __init__(self,value=None):
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
            temp = self.tail
            self.tail.next = new_node
            new_node.prev = temp
            self.tail = new_node
        self.length += 1
    def print_list(self):
        """Function to print the linked list
        """
        print("Linked List: ")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1