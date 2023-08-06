"""
    A queue is an abstract data type that serves as an ordered collection of elements. A simple queue will have several operations:

    queue.push(item) -> adds an item to the tail of the queue
    queue.pop() -> removes and returns an item from the head of the queue
    queue.peek() -> returns an item from the head of the queue
    queue.size() -> returns the number of items in the queue

    The storing method of a queue is First In - First Out

"""

class Queue:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		if len(self.items) == 0:
			return None
		temp = self.items[-1]
		del self.items[-1]
		return temp

	def peek(self):
		if len(self.items) == 0:
			return None
		return self.items[-1]

	def size(self):
		return len(self.items)