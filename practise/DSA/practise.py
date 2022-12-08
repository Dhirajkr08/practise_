#check length
#x=str(input())
#print(len(x))

#Float round
#x=float(input())
#print(round(x,2))

#check sum of digit
#x=int(input())
#sum=0
#for i in range(x):
#    i=x%10
#    sum=sum+i
#    x=x//10
#print(sum)


#split word
#x=str(input())
#for i in x:
#    print(i)
    
#range
#num=int(input())
#for i in range(2,100,2):
#    print(i)


# fibonacci series
#x=int(input())
#a=0
#b=1
#print(a)
#print(b)
#for i in range(0,x):
#    sum=a+b
#    a=b
#    b=sum
#print(sum)  

#x=int(input())# sum of digits
#sum=0
#for i in range(0,x):
#    i=x%10
#    sum=sum+i
#    x=x//10
#print(sum)    

#palindrome checking
#x=int(input())
#temp=x
#rev=0
#while x>0:
#    i=x%10
#    rev=rev*10+i
#    x=int(x/10)
#if rev==temp:
#    print("this is a palindrome") 
#else:
#    print("this is not a palindrome")       

#str1=input()
#str2=input()
#str1=str1.lower()
#str2=str2.lower()
#if(sorted(str1)==sorted(str2)):
#    print("this is an anagram")
#else:
#    print("this is not an anagram")
# 

#string1=input()# check anagram
#string2=input()
#string1=string1.lower()
#string2=string2.lower()
#if(sorted(string1)==sorted(string2)):
#    print("this is an anagram")
#else:
#    print("this is not an anagram")           

#string=input()
#pattern=str(input())
#if (string.lower().startswith(pattern.lower())or
#string.lower().endswith(pattern.lower())):
#    print("{} belongs to {}".format(string,pattern))
#else:
#    print("{} does not belongs to {}".format(string,pattern))

#str=input()
#for i in str:
#    print(i)

def sort_array(arr,length):
    for i in range(len(arr)-1):
        for j  in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                d=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=d

           
    return arr
def main():
    n=int(input())
    arr=[]
    for i in range(0,n):
        arr.append(int(input())) 
        output=sort_array(arr,n)
    for i in range(0,n):
        print(output[i])
main()                       