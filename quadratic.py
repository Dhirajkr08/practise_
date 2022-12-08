import cmath
a = float(input("enter the number"))
b = float(input("enter the second number"))
c = float(input("enter the third number"))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d)/(2*a))
sol2 = (-b+cmath.sqrt(d)/(2*a))
print("the quadratic equation is",(sol1,sol2))
