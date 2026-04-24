# Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.
def rearrange_alternately(arr):
    arr.sort()
    result = []
    i, j = 0, len(arr) - 1
    while i <= j:
        if len(result) % 2 == 0:
            result.append(arr[j])
            j -= 1
        else:
            result.append(arr[i])
            i += 1
    return result

print(rearrange_alternately([1, 2, 3, 4, 5, 6]))