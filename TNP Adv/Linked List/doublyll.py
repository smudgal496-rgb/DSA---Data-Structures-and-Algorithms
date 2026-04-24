class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_between(self, data, target_data):
        temp = self.head
        while temp and temp.data != target_data:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            new_node.prev = temp
            if temp.next is not None:
                temp.next.prev = new_node
            temp.next = new_node
        else:
            print("Target Node not found!")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def delete_node(self, key):
        temp= self.head
        if not temp:
            print("List is empty!")
            return
        
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        
        while temp and temp.data != key:   
            temp = temp.next

        if not temp:
            print("Node with data", key, "not found!")
            return
        
        if temp.next:
            temp.next.prev = temp.prev
        
        if temp.prev:  
            temp.prev.next = temp.next


'''
    def delete_at_start(self):
        if not self.head:
            print("List is empty!")
            return
        print ("Deleted Node is:", self.head.data)
        self.head = self.head.next 
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            print ("Deleted Node is:", self.head.data)
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        print ("Deleted Node is:", temp.data)
        temp.prev.next = None

    def delete_in_between(self, key):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            print("Node with data", key, "not found!")
            return
        print ("Deleted Node is:", temp.data)
        if temp.prev:
            temp.prev.next = temp.next
        else:  # Deleting the head node
            self.head = temp.next
        if temp.next:
            temp.next.prev = temp.prev

'''

dll= DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_start(5)
dll.insert_at_between(15, 10)
dll.display()   

dll.delete_node(20)
dll.display()