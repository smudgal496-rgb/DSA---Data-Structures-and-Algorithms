# Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

def printLeaders(arr,size): 
    
    for i in range(0, size): 
        for j in range(i+1, size): 
            if arr[i]<=arr[j]: 
                break
        if j == size-1: 
            print(arr[i], end=" ") 

 
arr=[16, 17, 4, 3, 5, 2] 
printLeaders(arr, len(arr)) 

