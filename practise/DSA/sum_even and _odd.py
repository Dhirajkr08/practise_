n=int(input())
sum_odd=0
sum_even=0
while n>0:
    sum=n%10
    if sum%2==0:
        sum_even=sum_even+sum
    else:
        sum_odd=sum_odd+sum
    n=n//10
print(sum_even)
print(sum_odd)            