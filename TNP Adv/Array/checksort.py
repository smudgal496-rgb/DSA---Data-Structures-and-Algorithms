# Check if Array is Sorted
def check_sorted(arr):
    length = len(arr)
    for i in range(length - 1):
        if arr[i] > arr[i + 1]:
            print("Array is not sorted.")
            return
    print("Array is sorted.")
        
check_sorted([1, 2, 3, 6, 4, 5])
check_sorted([1, 2, 3, 4, 5, 6])
        