from math import sqrt

a = int(input("enter coeficient of first term(a)"))
b = int(input("enter coeficient of first second(b)"))
c = int(input("enter coeficient of first third(c)"))
w = sqrt((b**2)-4*a*c)
def find_roots(a,b,c):
    y_1 = (-b + w) /2*a
    y_2 = (-b - w) /2*a
    print("the roots of the quadratic equations are :",y_1,y_2)
find_roots(a,b,c)
    
    