def duplicate_elements_hashing(arr):
    element_count = {}
    duplicates = []

    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1

    for num, count in element_count.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

arr = [1, 2, 3, 4, 2, 5, 1]
result = duplicate_elements_hashing(arr)
print("Duplicate elements:", result)