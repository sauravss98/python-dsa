from queues import Queue

queue1 = Queue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.print_queue()
queue1.dequeue()
queue1.print_queue()