x=int(input())
temp=x
rev=0
while x>0:
    i=x%10
    rev=rev*10+i
    x=int(x/10)
if temp==rev:
    print("this is a palindrome")
else:
    print("this is not a palindrome")        