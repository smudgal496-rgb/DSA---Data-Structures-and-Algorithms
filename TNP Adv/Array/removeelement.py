# Remove the given element from the array
def removeelement(arr,ele):
    if ele not in arr:
        print ("Element not in array")
        print (arr)
    else:
        arr.remove(ele)
        return arr
print(removeelement([10,4,18,46,52],16))
