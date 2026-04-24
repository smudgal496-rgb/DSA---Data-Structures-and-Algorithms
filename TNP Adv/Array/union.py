# Find Union of Two Arrays
def union(arr1, arr2):
    un=arr1+arr2
    un=list(set(un))
    return un

def union_bitwise(arr1, arr2):
    a= set(arr1)
    b= set(arr2)
    c= a | b
    return list(c)

print("Union=",union([1, 2, 3, 3, 4, 5], [3, 4, 5, 6, 7, 8]))
print("Union using bitwise=",union_bitwise([1, 2, 3, 3, 4, 5], [3, 4, 5, 6, 7, 8]))