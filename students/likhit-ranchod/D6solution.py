#problem1

def is_leap_year(year):
    if year%4==0 and year%100!=0:
        print("true")
    else:
        print("false")
year=int(input("enter a year:"))
is_leap_year(year)

#problem2

def classify_grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

score=int(input("Enter yor score:"))
classify_grade(score)
