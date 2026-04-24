# Find Intersection of Two Arrays: Find the common elements between two arrays.

def intersection(arr1, arr2):
    co=[]
    for i in arr1:
        for j in arr2:
            if i == j:
                co.append(i)
    co=list(set(co))
    return co

print("Intersection=",intersection([1, 2, 3, 3, 4, 5], [3, 4, 5, 6, 7, 8]))