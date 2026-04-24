from collections import deque

def is_pall_queue(word):
    q= deque(word)

    while len(q) >1:
        if q.popleft() != q.pop():
            return False
    return True

st= "manan"
if is_pall_queue(st):
    print ("Pallindrome")   
else:    print ("Not Pallindrome")    