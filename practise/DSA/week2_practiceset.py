#Q1!
"""
x=str(input())
count=0
for char in x:
    if char.lower() in['a','e','i','o','u']:
        count=count+1
print(count)  """

#Q2
"""
x=int(input("enter your number:"))
for i in range(2,x):
    if (x%i)==0:
       print("ths is not a prime number")
    break   
else:
    print("this is a prime number")
"""
#Q3
"""
word=str(input("word:"))
ch=str(input())
word=word.replace(ch,"")
print(word)"""

#Q4
"""
string=str(input())
print(string[::-1])
"""
#Q5
"""
n=int(input("n:"))
sum=0
for i in range(n):
    i=n%10
    sum=sum+i
    n=n//10
print(sum) """

#Q6
"""
n=input()
num=n.split(',')
num=[int(number)for number in num]
start=num[0]
end=num[-1]
total=[i for i in range(start,end+1)]
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end="")  """

#Q7
"""
string=input()
w=str(input())
count=0
for i in string:
    if i == w:
        count=count+1
print(w,count) """    

#Q8
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
# practise:::set
"""
ls=['a','e','i','o','u']
string=" ".join(ls)
print(string)
"""

"""
ls=["one",'two',1,2,1.2,1.5,{"name":"Bunny"}]
print(ls)
"""

# for slicing
"""
print("\n slicing output")
print(ls[0:], ls[::-1], ls[2:4], sep-"\n")
"""

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
    print(max_count)  """

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

"""
sentence=str(input())
max_count=0
count=1
for i in range(len(sentence)-1):
    if sentence[i]==sentence[i+1]:
        count=count+1
        max_count=max(max_count,count)
        count=1
        max_count=max(max_count,count)
if max_count>1:
    print(max_count)
"""

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
    max_count =max(max_count,count)
if max_count>1:
    print(max_count)        
  """

  # max count
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

# frequency max_count
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
    print(max_count)  """

#find missing in line
"""
n=input()
num=n.split(",")
num=[int(number)for number in num]
start=num[0]
end=num[-1]
total=[i for i in range(start,end)]
missing=list(set(total).difference(set(num)))
for i in missing:
    print(i,end=',')   
"""
# count vowels:
"""
string=input()
count=0
for i in string:
    if i.lower() in ['a','e','i','o','u']:
        count=count+1

print(count) """ 

# count each word present in word
"""def count_vow(string):
    string=string.casefold()
    count={}
    for char in string:
        if char in count:
            count[char]=count[char]+1
        elif char=='a'or'e' or 'i' or 'o' or 'u':
            count[char]=1
    return count
string=input()    
if len(count_vow(string))==0:
    print("No vowels found")
else:
    print(count_vow(string)) """                  

## count each vowel
"""string=input()
for char in ['a','e','i','o','u']:
    count=0
    for i in string:
        if i.lower()==char:
            count=count+1
    print(char,count) """          