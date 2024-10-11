""" File for linked list
"""
from linked_list.node import Node

class LinkedList:
    """Linked list class
    """
    def __init__(self, value=None):
        """Constructor

        Args:
            value (_type_, optional): _description_. Defaults to None.
        """
        self.head = None
        self.tail = None
        self.length = 0

        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
    def append(self,value):
        """Function to append

        Args:
            value (_type_): _description_
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def prepend(self,value):
        """Function to add value to first of linked list

        Args:
            value (_type_): _description_
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    def print_list(self):
        """Function to print the linked list
        """
        print("Linked List: ")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
