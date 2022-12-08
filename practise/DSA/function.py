"""
a=10 #global variable
def f1():
    a=20 # local vaiable
    print(a)
def f2():
    print(a) 
f1()
f2()  
"""

"""
def ibi(n):
    if n==0:
       return 0 
    elif n==1:
        return 1
    else:
        return ibi(n-1)+ibi(n-2)
def fibi(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        return a 
"""

"""def increment(a):
    a=a+1
    num=1
    increment(num)
    num"""

"""def display(name,course="btech"):
    print(name)
    print(course)
display(name="Dhiraj",course="btech") 
display(name="Bunny")       
"""

"""
ls=['a','e','i','o','u']
string="".join(ls)
print(string)
"""


