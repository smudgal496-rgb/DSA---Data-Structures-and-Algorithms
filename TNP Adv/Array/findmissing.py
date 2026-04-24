# Find the missing number from an array where length of array is from 1 to n
def findmissingnumber(arr):
  n=len(arr)+1
  summ= sum(arr)
  expected_sum= (n*(n+1))//2
  missing= expected_sum-summ
  return missing

print(findmissingnumber([1,2,3,5,6]))
