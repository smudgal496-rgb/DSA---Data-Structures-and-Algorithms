# Merge Two Arrays

def mergeArrays(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    return arr

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(mergeArrays(arr1, arr2))  