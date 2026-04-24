class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        new_node.next = self.head
        self.head = new_node
        new_node.next = self.head

    def insert_at_end(self, data):
        new_node = Node(data)
    
    # Case 1: Empty list
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Point to itself (circular)
            return
    
    # Case 2: Traverse to last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

    # Insert new node at end
        temp.next = new_node
        new_node.next = self.head

    def insert_at_between(self, data, target_data):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        while True:
            if temp.data == target_data:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print (f"{target_data} not found in the list!")

    def display(self):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()
        

    def delete_start(self):
        if not self.head:
            print("List is empty!")
            return
        print ("Deleted Node is:", self.head.data)
        if self.head.next == self.head:  # Only one node in the list
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def delete_end(self):
        if not self.head:
            print("List is empty!")
            return
        
        if self.head.next == self.head:
            print ("Deleted Node is:", self.head.data)
            self.head = None
        else:
            curr= self.head
            prev= None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
        prev.next = self.head
        print ("Deleted Node is:", curr.data)

    def delete_value(self, key):
        if not self.head:
            print("List is empty!")
            return
        
        curr = self.head
        prev = None

        if curr.data == key:
            self.delete_start()
            return
        
        while True:
            if curr == self.head:
                print (f"Node with data {key} not found in the list!")
                break
            if curr.data == key:
                prev.next = curr.next
                print ("Deleted Node is:", curr.data)
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break
        print (f"Node with data {key} not found in the list!")


cll= CircularSinglyLinkedList()
cll.insert_at_end(10)         
cll.insert_at_end(20)
cll.insert_at_start(5)
cll.insert_at_between(15, 10)
cll.display()