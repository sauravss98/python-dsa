from double_linked_list import DoubleLinkedList

list1 = DoubleLinkedList(1)
list1.append(2)
list1.append(3)
list1.prepend(5)
list1.print_list()
print(list1.head.value)