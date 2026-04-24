# Rotate Array by k Positions: Rotate the array to the right by k positions.

def rotate_right(arr, k):
    k = k % len(arr)  #k is greater than array length
    rotated_arr = arr[-k:] + arr[:-k]
    print("Rotated Array:", rotated_arr)   

rotate_right([1, 2, 3, 4, 5, 6, 7], 3)