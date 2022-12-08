


n=int(input("n:"))
minimum=0
maximum=0
total=0.0
count=0
for i in range(n):
    num=int(input())
    count=count+1
    total=total+num
    if (i==0):
        minimum=num
    if num<minimum:
        minimum=num
    elif num>maximum:
        maximum=num
print("average",total/n)
print("maximum",maximum)
print("minimum",minimum)            
