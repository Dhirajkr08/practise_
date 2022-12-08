'''def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
def main():
    n=int(input())
    print_pattern(n) 
main()               
'''

"""
def print_pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for j in range(1,i+1):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        print()
def main():
    n=int(input())
    print_pattern(n)
main() """  

"""def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
def main():
    n=int(input())
    print_pattern(n)
main() """

"""
x=int(input())
temp=x
rev=0
while x>0:
    i=x%10
    rev=rev*10+i
    x=x//10
if temp==rev:
    print("this is a palindrome") 
else:
    print("this is not a palindrome")       
"""

"""
x=int(input("Enter the number:"))
temp=x
rev=0
while x>0:
    i=x%10
    rev=rev*10+i
    x=x//10
if temp==rev:
    print("This is a palindrome")
else:
    print("this is not a palindrome")    
"""

"""
x=str(input())
if (x==x[::-1]):
    print("this is a palindrome")
else:
    print("this is not a palindrome") 
"""    

