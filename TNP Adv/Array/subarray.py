# Find Subarray with Given Sum.
def subarray(arr, s):
    for i in range(len(arr)):
        sum=0
        for j in range(i, len(arr)):
            sum+=arr[j]
            if sum==s:
                return arr[i:j+1]
    return -1

print(subarray(arr=[1, 2, 3, 7, 5],s= 12))