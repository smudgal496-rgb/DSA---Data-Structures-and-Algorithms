# WAP to check that given queue is symmetrical
from collections import deque

def is_sym(arr):
    n=len(arr)
    front = 0 
    rear = n-1

    while front < rear:
        if arr[front] != arr[rear]:
            return False
        front += 1
        rear -= 1  
    return True

arr= [1,2,3,4,2,1]
if is_sym(arr):     print ("Symmetrical")
else:    print ("Not Symmetrical")