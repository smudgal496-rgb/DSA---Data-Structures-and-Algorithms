class SimpleQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def enqueue(self, element):
        if len(self.queue) < self.size:
            self.queue.append(element)
            print (f"Enqueued: {element}")
        else:
            return "Queue is overflow!"
    
    def dequeue(self):
        if not self.queue:
            return "Queue is underflow!"
        return self.queue.pop(0)
    
    def display(self):
        return self.queue
    
q= SimpleQueue(4)

q.enqueue(1)
q.enqueue(2)        
q.enqueue(3)
q.enqueue(4)
print(q.display())
q.dequeue()
print(q.display())


class LinearQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.capacity - 1
    
    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def enqueue(self, element):
        if self.is_full():
            return "Queue is overflow!"
        
        if self.front == -1:
            self.front += 1

        self.rear += 1 
        self.queue[self.rear] = element
        print (f"Enqueued: {element}")
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is underflow!"
        
        element = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
        
        self.front += 1
        
        return element
    
    def peek(self):
        if self.is_empty():
            return "Queue is underflow!"
        
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            return "Queue is underflow!"
        
        return self.queue[self.front:self.rear + 1]
    
lq = LinearQueue(4)
lq.enqueue(1)
lq.enqueue(2)       
lq.enqueue(3)
lq.enqueue(4)
print(lq.display())
lq.dequeue()
lq.dequeue()
print(lq.display())