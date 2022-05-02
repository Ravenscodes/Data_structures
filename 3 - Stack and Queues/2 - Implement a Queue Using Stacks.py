"""
You have to implement the enqueue() and dequeue() functions using the MyStack class we created earlier.
enqueue( ) will insert a value into the queue and dequeue( ) will remove a value from the queue.

Input
enqueue( ): A value to insert into the queue
dequeue( ): Does not require any input

Output
enqueue( ): Does not return anything
dequeue( ): Pops out and returns the oldest value in the queue

Sample Input
value = 5 # [1, 2, 3, 4]
enqueue(value)
dequeue()

Sample Output
True # [1, 2, 3, 4, 5]
1 # [2, 3, 4, 5]
"""

from Stack import MyStack


class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # inserting the value in the queue
            self.main_stack.push(value)
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    def dequeue(self):
        # If stack empty then return None
        if self.main_stack.is_empty():
            return None
        value = self.main_stack.pop()
        return value


queue = NewQueue()
for i in range(5):
    queue.enqueue(i+1)
print("----------")
for i in range(5):
    queue.dequeue()