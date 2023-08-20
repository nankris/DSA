# implementing enque using 2 stacks

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
    
    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(value)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            
# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())
