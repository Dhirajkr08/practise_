#fibonacci series
"""
n=int(input("n:"))
a=0
b=1
print(a)
print(b)
for i in range(n):
    sum=a+b
    a=b
    b=sum
print(sum) 
"""

#factorial
"""
n=int(input("n:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)
"""

#count digit
"""
string=input()
print(len(string)) 
""" 

#Sum of digit
"""
n=int(input("n:"))
sum=0
for i in range(n):
    i=n%10
    sum=sum+i
    n=n//10
print(sum)   
"""

#len word
"""
string=input()
print(len(string))
"""

#round float
"""
x=float(input())
print(round(x,2))
"""

##salary increment
"""
salary=int(input("salary:"))
if salary>=10000:
    salary=salary+salary*0.1
elif salary>=6000 and salary<10000:
    salary=salary+salary*0.05
elif salary<6000:
    salary=salary+salary*0.02
print(salary)            
"""

# prime number
"""
x=int(input())
for i in range(2,x):
    if x%i==0:
        print(x,"This is not a prime number")
        break
else:
    print(x,"this is not a prime number")    
"""

#odd even
"""
n=int(input())
if n%2==0:
    print("this is an even number",n)
    
else:
    print("this is not an even number",n)    
"""

#palindrome in string

"""
string=str(input())
if (string==string[::-1]):
    print("this is a palindrome")
else:
    print("this is not a palindrome")    
"""

# palindrome in integer
'''x=int(input())
temp=x
rev=0
while x>0:
    digit=x%10
    rev=rev*10+digit
    x=int(x/10)
if rev==temp:
    print("this is a palindrome") 
else:
    print("this is not a palindrome")             
'''

## count vowel
"""
string=input()
count=0
for char in string:
    if char.lower() in ['a','e','i','o','u']:
        count=count+1
print(count)        
"""

#count each vowel
"""
string=input()
for char in ['a','e','i','o','u']:
    count=0
    for i in string:
        if i.lower()==char:
            count=count+1
    print(char,count)
    """
# check anagram
"""
x=str(input())
y=str(input())
x=x.lower()
y=y.lower()
if  (sorted(x)==sorted(y)):
    print("this is an anagram")
else:
    print("this is not an anagram")              
"""

# sum_odd and sum_even
"""
x=int(input())
sum_odd=0
sum_even=0
while x>0:
    sum=x%10
    if sum%2==0:
        sum_even=sum_even+sum
    else:
        sum_odd=sum_odd+sum
    x=x//10
print(sum_even) 
print(sum_odd)     
"""

# split sentence
"""word=str(input())
for i in word:
    print(i)"""


# palindrome second method
'''word=str(input())
if (round(word==word)):
    print("this is a palindrome")
else:
    print("this is not a palindrome")'''

"""import math
print(math.radians(60))    
"""

"""
import math
print(math.pi)
"""

import mod
print(module)










