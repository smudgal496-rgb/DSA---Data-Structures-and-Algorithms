# Check if Two Arrays Are Equal: if two arrays contain the same elements
def arr_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Not Equal"
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return "Not Equal"
    return "Equal"

print(arr_equal([1, 2, 3, 4], [1, 2, 3, 4]))
print(arr_equal([1, 2, 3, 4], [1, 2, 3, 5]))