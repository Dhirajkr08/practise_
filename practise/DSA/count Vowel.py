#word=str(input("word:"))# for counthing the vowel

#count=0
#for i in word:
#   if i.lower() in['a','e','i','o','u']:
#    count=count+1
#print(count)
  

###### counting of  vowel:
#str=input("word:")
#count=0
#for i in str:
#    if i.lower() in ['a','e','i','o','u']:
#        count=count+1
#print(count)

## count of each vowel:
#sentence=str(input("word:"))
#for char in ['a','e','i','o','u']:
#    count=0
#    for letter  in sentence:
#        if letter.lower()==char:
#            count=count+1
#    print("{}-{}".format(char,count))        

#sentence=str(input())
#for char in ['a','e','i','o','u']:
#    count=0
#    for letter in sentence:
#        if letter.lower()==char:
#            count=count+1
#    print(char,count)        

#count number of vowel
#word=str(input())
#count=0
#for i in word:
#    if i.lower() in['a','e','i','o','u']:
#        count=count+1
#print(count)        

##count each vowel:
#sentence=str(input())
#for char in['a','e','i','o','u']:
#    count=0
#    for letter in sentence:
#        if letter.lower()==char:
#            count=count+1
#    print(char,count)        

# check vowels using def:

#def checkvowels(string):
#    string=string.casefold()
#    count={}
#    for character in string:
#        if character in count:
#            count[character]=count[character]+1
#        elif character=='a':
#           count[character]=1
#        elif character=='e':
#            count[character]=1
#        elif character=='i':
#            count[character]=1    
#        elif character=='o':
#            count[character]=1
#        elif character == 'u':
#            count[character]=1
#    return count
#string=str(input("Sentence:"))
#if (len(checkvowels(string)))==0:
#    print("No Vowels Found.")
#else:
#    print(checkvowels(string)) 
# 
"""
def checkvowels(string):
    string=string.casefold()
    count={}
    for character in string:
        if character in count:
            count[character]=count[character]+1
        elif character=='a':
            count[character]=1
        elif character=='e':
            count[character]=1
        elif character=='i':
            count[character]=1
        elif character=='o':
            count[character]=1
        elif character=='u':
            count[character]=1
    return count
string=str(input("sentence:"))
if len(checkvowels(string))==0:
    print("no vowels found.")
else:
    print(checkvowels(string))   """   
"""
def countvowels(string):
    string=string.casefold()
    count={}
    for char in string:
        if char in count:
            count[char]=count[char]+1
        elif char=='a':
            count[char]=1
        elif char=='e':
            count[char]=1
        elif char=='i':
            count[char]=1 
        elif char=='o':
            count[char]=1
        elif char=='u':
            count[char]=1
    return count
string=str(input())
if len(countvowels(string))==0:
    print("No Vowels Found.")
else:
    print(countvowels(string))
""" 
"""
x=int(input())
fact=1
i=1   
while i<=x:
    fact=fact*i
    i=i+1
print(fact)
"""

#check palindrome in integer::
"""
x=int(input())
rev=0
temp=x
while x>0:
    digit=x%10
    rev=rev*10+digit
    x=int(x/10)
if temp==rev:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
"""
# check palindrome in integer::
"""
x=str(input())
if(round(x==x)): #or if(x==x[::-1])
    print("this is a palindrome")
else:
    print("this is not a palindrom") 
"""       
# count digit
"""
x=int(input())
sum=0
for i in range(x):
    i=x%10
    sum=sum+i
    x=x//10
print(sum) 
"""  

# anagram
"""
x=str(input())
y=str(input())
x=x.lower()
y=y.lower()
if (sorted(x)==sorted(y)):
    print("this is an anagram")
else:
    print("this is not an anagram")
"""

#count vowel
"""
x=str(input())
count=0
for i in x:
    if i.lower() in ['a','e','i','o','u']:
        count=count+1
print(count)
"""
# count each vowel
"""
x=str(input())
for char in ['a','e','i','o','u']:
    count=0
    for letter in x:
        if letter.lower()==char:
            count=count+1
    print(count,char) 
"""
# count only present vowel:
"""
def countvowels(string):
    string=string.casefold()
    count={}
    for char in string:
        if char in count:
            count[char]=count[char]+1
        elif char=="a":
            count[char]=1 
        elif char=="e":
            count[char]=1 
        elif char=="i":
            count[char]=1 
        elif char=="o":
            count[char]=1 
        elif char=="u":
            count[char]=1 
    return count
string=input()
if len(countvowels(string))==0:
    print("No vowel Found")
else:
    print(countvowels(string))                        
"""
# check seperate word
"""
word=str(input())
for i in word:
    print(i)
""" 
string="hello"
print(string[id])
# print date
"""
date=input()
print("day",date[:2])
print("month",date[2:4])
print("year",date[:4])
"""

# count sentece
"""
sentence=str(input())
print(len(sentence))
"""
# print letter in odd position
"""
word=str(input())
print(word[::2])
"""



#print letter in even position

"""
word =str(input())
print(word[1::2])
"""


# print reverse

"""
word=str(input())
print(word[::-1])
"""
s