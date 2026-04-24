def valid_paranthesis(symbols):
    stack=[]
    mapping= {')':'(' , '}':'{' , ']':'['}

    for char in symbols:
        if char in mapping:
            top_ele= stack.pop() if stack else '#'
            if mapping[char] != top_ele:
                return False
        else:
            stack.append(char)
            
    return len(stack) == 0
        
symbols= "([]){}[]"
result= valid_paranthesis(symbols)
if result:
    print ("Valid Paranthesis")
else:
    print ("Invalid Paranthesis")