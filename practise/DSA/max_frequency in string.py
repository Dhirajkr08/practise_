"""
sentence=input()
max_count=0
count=1
for i in range(len(sentence)-1):
    if sentence[i]==sentence[i+1]:
        count=count+1
    else:
        max_count=(max_count,count)
        count=1
        max_count=(max_count,count)
if max_count>1:
    print(max_count,end='')  """

"""
sentence=str(input())
max_count=0
count=1
for i in range(len(sentence)-1):
    if sentence[i]==sentence[i+1]:
        count=count+1
    else:
        max_count=max(max_count,count)
        count=1
    max_count=max(max_count,count)
if max_count>1:
    print(max_count,end='')  
 """
# find missing number from same line :;
"""
n=input()
num=n.split(",")
num=[int(number) for number in num]
start=num[0]
end=num[-1]
total=[i for i in range(start,end)]
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end=",")                            
    """
 #find missing number from line:::
"""
n=input()
num=n.split(",")
num=[int(number)for number in num]
start=num[0]
end=num[-1]
total=[i for i in range(start,end)]
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end=",")
    """

"""
n=input()
num=n.split(",")
num=[int(number)for number in num] 
start=num[0]
end=num[-1]
total=[i for i in range(start,end)]
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end=",")   

"""

# count max frequency
"""
word=input()
max_count=0
count=1
for i in range(len(word)-1):
    if word[i]==word[i+1]:
        count=count+1
    else:
        max_count=max(max_count,count)
        count=1
    max_count=max(max_count,count)
if max_count>1:
    print(max_count) 
    """

#fibonaci series:
"""
num=int(input())
a=0
b=1
for i in range(0,num):
    sum=a+b
    a=b
    b=sum
print(sum) 
"""
#factorial
"""
num=int(input())
fact=1
i=1 
while i<=num:
    fact=fact*i
    i=i+1
print(fact)  
"""

"""
num=int(input())
fact=1
i=1
while i <=num:
    fact=fact*i
    i=i+1
print(fact) 
"""

# fibonacci series:
"""
num=int(input())
a=0
b=1
for i in range(0,num):
    sum=a+b
    a=b
    b=sum
print(sum)  
"""

#count digit:
"""
word =str(input())
print(len(word))
"""

#sum of numbers:
"""
num=int(input())
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)
"""
# count integers:
"""
num=int(input())
count=0
while num>0:
    digit=num%10
    count=count+1
    num=num//10
print(count)   
"""
## count vowels




 
         


