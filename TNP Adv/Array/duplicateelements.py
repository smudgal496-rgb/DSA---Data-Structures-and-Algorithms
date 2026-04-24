#Find Duplicate elements from an array
def duplicates(arr):
    n=len(arr)
    c=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                c.append(arr[i])
    c=list(set(c))
    return c
    
print (duplicates([1,2,3,4,4,4,5,5,6,7,8,8]))

def duplicates_hashing(arr):
    seen = set()
    dup = set()
    
    for num in arr:
        if num in seen:
            dup.add(num)
        else:
            seen.add(num)
    
    return list(dup)
print (duplicates_hashing([1,2,3,4,4,4,5,5,6,7,8,8]))
