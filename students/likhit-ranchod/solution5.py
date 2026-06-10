#problem

def rectangle(l,b):
    return l*b
    
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
    
a=rectangle(l,b)
print("Area is:",rectangle(l,b))

#problem2

m=int(input("No of members:"))
d={}
for x in range(m):
    name=input("Name of members")
    age=int(input("Enter age"))
    d.update({name:age})
print(d)
