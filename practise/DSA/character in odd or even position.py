# print for odd position
"""
num=str(input("num:"))
print(num[::2])
"""

#print for even position
"""
num=str(input("num:"))
print(num[1::2])
"""

# print reverse
"""
word=str(input())
print(word[::-1])
"""

# print reverse in integer:
"""
x=int(input())
rev=0
while x!=0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
print(rev)   
"""
#or
x=int(input())
temp=x
rev=0
while x>0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
print(rev)  

