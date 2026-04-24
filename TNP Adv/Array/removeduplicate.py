#  Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))