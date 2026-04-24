# Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
def find_pair_normal(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
    return None

def find_pair_hashing(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            print(complement, num)
        seen.add(num)
    return None

find_pair_hashing([1, 2, 3, 4, 5], 9)
find_pair_normal([1, 2, 3, 4, 5], 9)