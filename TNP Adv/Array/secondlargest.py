#Find the Second Largest Element

def second(arr): 
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        print("There is no second largest element.")
        return
    unique_arr.sort()
    print("Second Largest Element:", unique_arr[-2])

second([13, 1, 4, 1, 55, 91, 2, 16, 55, 3, 5])


