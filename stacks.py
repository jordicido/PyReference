"""
    A stack is an abstract data type that serves as a collection of elements. Our stack will have several operations:

    stack.push(item) -> places a new item on top of the stack
    stack.pop() -> removes the top item from the stack and returns it
    stack.peek() -> returns the top item from the stack without modifying the stack
    stack.size() -> returns the number of items in the stack

    The storing method of a stack is Last In - First Out

"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    