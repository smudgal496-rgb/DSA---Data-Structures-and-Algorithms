# Implement Stack with Linked List


# Define custom exception
class IsEmptyError(Exception):
    pass


# Define Node class
class Node:
    def __init__(self, element, _next):
        self.element = element
        self._next = _next


# Define Stack class
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.head = Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IsEmptyError("This stack is empty, therefore cannot pop.")
        result = self.head.element
        self.head = self.head._next
        self.size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise IsEmptyError("Stack is empty, so cannot retrieve any elements.")
        return self.head.element


# Testing the stack
if __name__ == "__main__":
    s = Stack()

    for i in range(1,100000):
        s.push(i)

    print("Top element:", s.top())
    for i in range (1,500):
        print("Popped element:", s.pop())
    print("Top element after pop:", s.top())  
    print("Stack size:", len(s)) 
