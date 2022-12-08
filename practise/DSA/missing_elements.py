"""
n=input()
num=n.split(",")
num=[int(number) for number in num]
start=num[0]
end=num[-1]
total=[i for i in range (start,end+1)]
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end=",")
    """

"""
n=input()
num=n.split(" ")
num=[int(number) for number in num]
start=num[0]
end=num[-1]
total=[i for i in range(start,end)]
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end=",") 
    """

n=input()
num=n.split()
num=[int(number)for number in num]
start=num[0]
end=num[-1]
total=[i for i in range(start,end)] 
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end=',')      
