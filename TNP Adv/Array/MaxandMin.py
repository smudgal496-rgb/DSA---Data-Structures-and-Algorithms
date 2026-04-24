#Find the Maximum & Minimum Element

def find_max_min(arr):
    max_element = arr[0]
    min_element = arr[0]
    
    for i in range(0, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
        elif arr[i] < min_element:
            min_element = arr[i]
    
    print("Maximum Element:", max_element)
    print("Minimum Element:", min_element)

find_max_min([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])