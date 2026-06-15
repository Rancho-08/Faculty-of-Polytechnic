#problem1

def dupl(l): 
    s = set() 
    for x in l: 
        if x in s: 
            return True
        else: 
            s.update({x})
    return False  

user_input = input("Enter elements: ").split()
print(dupl(user_input))
