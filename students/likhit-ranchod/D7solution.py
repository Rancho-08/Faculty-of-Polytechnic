#problem1

def sum_to_n(n):
    total = 0  

    for i in range(1, n + 1):
        total =total+ i

    print(total)
n=int(input("Enter number:"))
sum_to_n(n)

#problem2

def times_table(n):
    for i in range (1,11):
        print(f"{n} x {i} = {n * i}")
n=int(input("enter the number:"))
times_table(n)
