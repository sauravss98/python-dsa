"""  Test File
"""
from linked_list.linked_list import LinkedList

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.prepend(5)
linked_list.append(205)
linked_list.prepend(33)
linked_list.print_list()

new_linked_list = LinkedList()
new_linked_list.append(6)
new_linked_list.append(7)
new_linked_list.append(8)
new_linked_list.append(9)
new_linked_list.prepend(10)
new_linked_list.append(11)
new_linked_list.prepend(12)
new_linked_list.print_list()
