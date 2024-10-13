"""File for node
"""
class Node:
    """Class for Node
    """
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def set_next(self, next_node):
        """Sets the next node"""
        self.next = next_node

    def get_next(self):
        """Returns the next node """
        return self.next
