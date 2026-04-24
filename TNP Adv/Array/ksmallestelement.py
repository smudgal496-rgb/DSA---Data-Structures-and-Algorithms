# Find the Kth Smallest Element
def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

print(kth_smallest([7, 10, 4, 3, 20, 15], 3))