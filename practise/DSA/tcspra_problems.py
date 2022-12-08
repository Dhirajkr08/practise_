#string=input()
#for i in string:
#    print(i)


#sum of digit
#integer=int(input())
#sum=0
#for i in range(integer):
#    i=integer%10
#    sum=sum+i 
#    integer=integer//10
#print(sum)       


#Q3
#num=float(input())
#print(round(num,2))

#Q4
#exp=str(input())
#print(len(exp))

#Q4
#num=int(input())
#if num>0 and num%2==0:
#    print(num,"this is an even natural number")
#elif num>0 and num%2 !=0:
#    print(num,"this is odd natural number")
#elif num%2==0:
#    print(num,"this is an even number")
#else:
#    print("this is an odd number")
    
#Q6:
# x=str(input("x:"))
#pattern=str(input("pattern:"))
#if (x.lower().startswith(pattern.lower())or
#x.lower().endswith(pattern.lower())):
#    print("{} contains {}".format(x,pattern))
#else:
#    print("{} does not contain {}".format(x,pattern))  

#salary=int(input("salary:"))
#if salary>=10000:
#    salary=salary+salary*0.1
#elif salary>=6000 and salary<10000:
#    salary=salary+salary*0.08
#elif salary<6000:
#    salary=salary+salary*0.05
#print(salary)            

#a=int(input("a:"))
#b=int(input("b"))
#char=int(input())
#if(char==1):
#    print("{}+{}={}".format(a,b,a+b))
#elif(char==2):
#    print("{}-{}={}".format(a,b,a-b))
#elif(char==3):
#    print("{}*{}={}".format(a,b,a*b))
#elif(char==4):
#    print("{}^{}={}".format(a,b,a**b))
#else:
#    print("No choice found")    

#string=input("Word:")
#if(string==string[::-1]):
#    print("this is  a palindrome")
#else:
#    print("this is not a palindrome")    

#anagram
str1=input("Word1:")
str2=input("word2:")
str1=str1.lower()

str2=str2.lower()
if (sorted(str1)==sorted(str2)):
    print("this is an anagram")
else:
    print("this is not an anagram")    

