


#fibbonacci Series
n=int(input("n:"))
a=0
b=1
print(a)
print(b)
for i in range(0,n):
    sum=a+b
    a=b
    b=sum
print(sum)    
