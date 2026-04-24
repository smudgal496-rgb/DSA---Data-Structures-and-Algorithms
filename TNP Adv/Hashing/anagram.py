def isAnagram(s,t):
    if len(s) != len(t):
        return False
    count = {}

    for i in s:
        count[i] = count.get(i,0)+1
    for i in t:
        count[i] = count.get(i,0)-1
    
    for val in count.values():
        if val !=0:
            return False
        else:
            return True
       
s=input("Enter the first string: ")
t=input("Enter the second string: ")
if isAnagram(s,t):
    print("The strings are anagrams.")
else:    
    print("The strings are not anagrams.")