'''
Merger two sorted LL and create a new merged sorted LL
    L1= [1,2,4]
    L2= [1,3,4]
    Output: [1,1,2,3,4,4]  
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
We will use dummy node 
Set tail pointer in dummy node
Iterate till nodes in sorted LL
    If l.data <= l2.data
        tail.next = l1
        l1 = l1.next
    else:
        tail.next = l2
        l2 = l2.next
    tail = tail.next
    tail= []
    If l1 is not None
        tail.next = l1
    elif l2 is not None
        tail.next = l2
'''
def mergeTwoLists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

L1= Node(1)
L1.next = Node(2)
L1.next.next = Node(4)
L2= Node(1)
L2.next = Node(3)
L2.next.next = Node(4)
merged_head = mergeTwoLists(L1, L2)
print("Merged Linked List:", end=" ")
printList(merged_head)

#time complexity: O(n+m) where n and m are the lengths of the two linked lists
#space complexity: O(1) since we are not using any extra space for merging,