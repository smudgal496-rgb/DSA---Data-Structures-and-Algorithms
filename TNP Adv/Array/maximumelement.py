# Find Majority Element: Find the element that appears more than n/2 times.
def majority_element(arr):
    n=len(arr)
    for i in range(n):
        count=1
        for j in range (i+1,n):
            if arr[i]==arr[j]:
                count+=1
        if count>n/2:
            return arr[i]   
        
print(majority_element([2, 2, 1, 1, 1, 2, 2, 1, 2, 9, 9,9 ,9,9,9,9,9,9,9,9]))