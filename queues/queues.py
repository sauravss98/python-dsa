from node import Node
class Queue:
   def __init__(self,value=None):
      self.front = None
      self.back = None
      self.length = 0
      if value is not None:
         new_node = Node(value)
         self.front = new_node
         self.back = new_node
         self.length = 1
   
   def enqueue(self,value):
      new_node = Node(value)
      if self.length == 0:
         self.front = new_node
         self.back = new_node
      else:
         self.back.next = new_node
         self.back = new_node
      self.length += 1
   
   def dequeue(self):
      if self.length == 0:
         self.front = None
         self.back = None
      else:
         temp = self.front
         self.front = temp.next
      self.length -= 1
   
   def print_queue(self):
      print("Queue is ")
      temp = self.front
      while temp is not None:
         print(temp.value)
         temp = temp.next