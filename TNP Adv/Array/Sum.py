#Find the Sum of Elements

def sum_elements(arr):
    s = 0
    for i in range(len(arr)):
        s= s+ arr[i]
    print("Sum of Elements:", s)

sum_elements([1, 2, 3, 4, 5])