class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    def insert_at_between(self, data, target_data):
        temp = self.head
        while temp and temp.data != target_data:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Target Node not found!")

    def delete_at_start(self):
        if not self.head:
            print("List is empty!")
            return
        self.head = self.head.next 

    def delete_at_end(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            print ("Deleted Node is:", self.head.data)
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        print ("Deleted Node is:", temp.next.data)
        temp.next = None

    def delete_in_between(self, key):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        if temp and temp.data == key:
            print ("Deleted Node is:", temp.data)
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print ("Key not found!")
        else:
            print ("Deleted Node is:", temp.data)
            prev.next = temp.next
        

    def display(self):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print("None")

    def search(self, key):
        if not self.head:
            print("List is empty!")
            return
        pos=0
        temp = self.head
        while temp:
            if temp.data == key:
                print("Element found at position:", pos)
                return
            temp = temp.next
            pos+=1
        print(f"{key}Element not found!")

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Total nodes in the list:", count)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


LL= SinglyLinkedList()
LL.insert_at_end(10)
LL.insert_at_end(20) 
LL.insert_at_end(30)
LL.insert_at_start(5) 
LL.insert_at_between(15, 10)
LL.display()
LL.reverse()
LL.display()
LL.search(20)