from collections import deque

def generate_binary(n):
    q= deque(['1'])
    res= []
    for _ in range(n):
        curr= q.popleft()
        res.append(curr)
        q.append(curr+'0')
        q.append(curr+'1')
    return res

print (generate_binary(20))