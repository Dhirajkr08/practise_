"""
number=int(input())
sum_even=0
sum_odd=0
while number>0:
    sum=number%10
    if sum%2==0:
        sum_even=sum_even+sum
    else:
        sum_odd=sum_odd+sum
    number=number//10
print("the sum of even digit is",sum_even)
print("the sum of odd digit is",sum_odd) 
"""

num=int(input("number:"))
sum_even=0
sum_odd=0
while num>0:
    sum=num%10
    if sum % 2==0:
        sum_even=sum_even+sum
    else:
        sum_odd=sum_odd+sum
    num=num//10
print("The sum of even digits is ",sum_even) 
print("the sum of odd digit is",sum_odd)           
