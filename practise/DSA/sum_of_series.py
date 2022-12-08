# Q1
"""
n=int(input())
sum=0.0
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(i/fact)
    n=n+1
print(round(sum,5)) 
"""

#Q2
x=int(input("N:"))
for i in range(2,x):
   if (x%i)==0:
    print(x,"is not a prime number")
    break    
else:
    print(x,"is  a prime number")

#Q3
    