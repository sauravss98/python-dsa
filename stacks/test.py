from stack import Stack

stack = Stack(1)
stack.push(2)
stack.push(3)
stack.print_stack()
print("popped value is",stack.pop())
stack.print_stack()
print("Top value of the stack is",stack.peek())