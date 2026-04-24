# Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
def moveZeroes(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            c=(arr.pop(i))
            arr.append(c)
    return arr

print(moveZeroes([0, 1, 0, 3, 12]))