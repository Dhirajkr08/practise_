## check armstrong number

num=int(input())
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print(" is an armstrong number",num)
else:
    print(" is not an armstrong number",num)        

