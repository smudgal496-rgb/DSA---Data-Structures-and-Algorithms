# Rotate Array to the Left by k Positions

def rotate_left(arr, k):
    k = k % len(arr)  #k is greater than array length
    rotated_arr = arr[len(arr)-k:] + arr[:len(arr)-k]  
    print("Rotated Array:", rotated_arr)   

rotate_left([1, 2, 3, 4, 5], 3)