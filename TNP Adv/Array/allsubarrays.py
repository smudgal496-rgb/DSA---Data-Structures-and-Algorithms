# Find All Subarrays
def all_subarrays(arr):
    subs = []
    n= len(arr)
    for i in range(n):
        for j in range(i, n):
            subs.append(arr[i:j+1])
    return subs

print(all_subarrays([1, 2, 3, 4, 5]))