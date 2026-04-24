from collections import deque

def reverse_string_queue(string):
    q= deque()
    for char in string:
        q.append(char)
    
    rev= ""
    
    while q:
        rev += q.popleft()
    return rev

print (reverse_string_queue("abcde"))

class Queue:
    def __init__(self):
        self.queue= []

    def enqueue(self,ele):
        self.q.append(ele)

    def isEmpty(self):
        return len(self.q) == 0
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is underflow!"
        ele = self.q[0]
        self.q= self.q[1:]
        return ele
    
def reverse_string_q(string):
    q= Queue()
    for char in string:
        q.enqueue(char)
    
    rev= ""
    n= q.size()

    for i in range(n):
        for j in range (n-i-1):
            q.enqueue(q.dequeue())
        rev += q.dequeue()
    return rev

print (reverse_string_q("abcde"))