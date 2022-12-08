"""
n=int(input())
largest_n=0
smallest_n=9
count=0
while n>0:
    sum=n%10
    count=count+sum
    if largest_n<n:
        largest_n=sum
    elif smallest_n>n:
        smallest_n=sum
    n=n//10
print(largest_n) 
print(smallest_n)
print(count) 
"""   

#again
from cgitb import small


n=int(input("n:"))
largest_n=0
smallest_n=9
count=0
while n>0:
    sum=n%10
    count=count+sum
    if largest_n<sum:
        largest_n=sum
    elif smallest_n>sum:
        smallest_n=sum
    n=int(n/10)
print(largest_n)
print(smallest_n)
print(count)        

    