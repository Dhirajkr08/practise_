# swapping two number:
"""def swapnumber(a,b):
    i=a
    a=b
    b=i
    print(a)
    print(b)
def main():
    a=int(input())
    b=int(input())
    swapnumber(a,b)
main()        """

# largest number
"""def largestnumber(a,b):
    if a>b:
        print(a)
    else:
        print(b)
def main():
    a=int(input())
    b=int(input())
    largestnumber(a,b)
main()                """

# largest number
"""
def largestnumber(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c) 
def main():
    a=int(input())
    b=int(input())
    c=int(input()) 
    largestnumber(a,b,c)
main() 
"""

# distance cost
"""
def distance_cost(d):
    if d>=1000:
        print(12)
    elif d>500 and d<1000:
        print(10)
    elif d>100 and d<=500:
        print(8)
    else:
        print(5)
    return
def main():
    d=int(input())
    distance_cost(d)
main() 
"""

#pass or fail using terenary operator
"""
def marks(n):
    print("pass") if n>=40 else print("fail")
def main():
    n=int(input())
    marks(n)
main()    
"""

# maximum using terenary operator
"""
def findmaximum(a,b):
    print(a)if a>b else print(b)
def main():
    a=int(input())
    b=int(input())
    findmaximum(a,b)
main() 
"""

#week days
"""
def weekdays(n):
    if n==1:
        print("monday")
    elif n==2:
        print("tuesday")
    elif n==3:
        print("wednesday")
    elif n==4:
        print("thrusday")
    elif n==5:
        print("friday")
    elif n==6:
        print("saturday")
    elif n==7:
        print("sunday")
    else:
        print("invalid")
def main():
    n=int(input())
    weekdays(n)
main() 
"""

# print output if x=2:
"""def choice(x):
    while x>0:
        if x==1:
            print(1)
            break
        elif x==2 or x==3 or x==4:
            print(2,3,4)
            break
        else:
            print("none")
            break 


def main():
    x=int(input())
    choice(x)
main()    
"""

# find even number using while loop 
"""
def find_even(n):
    i=2
    while n>=i:
        print(i)
        i=i+2

def main():
    n=int(input())
    find_even(n)
main()   
"""

# random series using while loop
"""def series(n):
    i=1
    while i*i<=n:
        print(i*i)
        i=i+1
def main():
    n=int(input())
    series(n)
main() 
"""

#print all number except 5:
"""def number(n):
    i=1
    while i <=n:
        print(i)
        i=i+1
        if i%5==0:
            i=i+1
            
def main():
    n=int(input())
    number(n)  
main()              
"""

# print digit of a number while loop
"""
def print_digit(n):
    while n>0:
        i=n%10
        n=n//10
        print(i)
def main():
    n=int(input())
    print_digit(n)
main()  
"""
# print digit from number using for loop
"""
def print_digit(n):
    for i in n:
        print(i)
def main():
    n=str(input())
    print_digit(n)
main()            
"""
#print armstrong number:
"""
def armstrong(n):
    temp=n
    sum=0
    while temp>0:
        i=temp%10
        sum=sum+i**3
        temp=temp//10
    if temp==sum:
        print("true")
    else:
        print("false")
def main():
    n=int(input())
    armstrong(n)
main()                    
"""

"""
def cheeck_reverse(n):
    rev=0
    temp=n
    while temp>0:
        i=temp%10
        rev=rev*10+i
        temp=int(temp/10)
    return rev
def main():
    n=int(input())
    ans=cheeck_reverse(n)
    print(ans)
main()    
"""

# find even number
"""def even_number(-1,n,1):
    for i in range(i+1):
        if i%2==0:
            print(i)
def main():
    n=int(input())
    even_number(n)
main()                
"""
# find odd number
"""def findodd_number(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
def main():
    n=int(input())
    findodd_number(n)
main()                
"""

#print series using for loop of cube or graadually increase:
"""
def find_series(n):
    for i in range(1,n):
        if i*i*i>n:
            break
        print(i*i*i)
def main():
    n=int(input())
    find_series(n)
main()                
"""

#print the series except divisible by 4
"""
def series(n):
    for i in range(0,n+1):
        if i%4==0:
            continue
        if i%2==0:
            print(i)
def main():
    n=int(input() )  
    series(n)
main()             
"""

# print the series till any other number break the loop
"""
def print_series(n,m):
    for i in range(1,n):
        if i==m:
            break
        print(i)
def main():
    n=int(input())
    m=int(input())
    print_series(n,m)
main()    
"""

#pattern left hand triangle

"""
def print_pattern(n):
    for i in range(0,n):
        str=""
        for j in range(0,i+1):
            str=str+"*"
        print(str)  
def main():
    n=int(input())
    print_pattern(n)          
main()
"""
# pattern opposite left hand triangle
"""
def print_pattern(n):
    for i in range(n):
        str=""
        for j in range(n-i):
            str=str+"*"
        print(str)
def main():
    n=int(input())
    print_pattern(n)
main()                
"""

# right hand triangle
"""
def print_pattern(n):
    for i in range(n):
        for j in range(1,n-i):
            print(" ",end="")
        for j in range(0,i+1):
            print("*",end="")
        print()
def main():
    n=int(input())
    print_pattern(n)
main()                   
"""

# reverse right hand triangle
"""
def print_pattern(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(n,i,-1):
            print("*",end="")
        print()
def main():
    n=int(input())
    print_pattern(n)
main()    
"""
# pyramid pattern
"""
def print_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()
def main():
    n=int(input())
    print_pattern(n)
main()                    
"""

#Reverse and normal pyramid
"""def print_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()    
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()    
def main():
    n=int(input())
    print_pattern(n)
main()    
"""
'''for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()    
    '''


"""
for i in range(5):
    print("",end="")
    for j in range(i+1):
        print("*",end="")
        
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")        
    print()
"""
'''
for i in range(4):
    str=""
    for j in range(8):
        if j<=0+i:
            str=str+"*"
    for j in range(4-i):
        str=str+""
    for j in range(8):
        if j<=0+i:
            str=str+"*" 
    print(str)   
'''
"""def print_series(n):
  i=1
  while i*i<=n:
    print(i*i)
    i=i+1
def main():
  n=int(input())
  print_series(n)
main()  
"""
'''
def find_prime(n):
    list=[]
    x=2
    while (len(list)<n):
        flag=1
        for i in range(2,x):
            if x%i==0:
                flag=0
                break
        if flag==1:
            list.append(i)
        x=x+1
    return list
def main():
    n=int(input())
    output=find_prime(n)
    for i in range(0,n):
        print(output[i])                
'''
#print prime number


# print n number of prime number
'''
n = int(input('Please enter n: '))
num=int(n)
x=2
cnt = 0
list=[]

while (len(list)<n):
    flag=1
    for i in range(2, x):     # prime test
        if x % i == 0:
            flag=0
            break
    if flag==1:    # was prime
        cnt += 1
        list.append(x)
    if cnt == n:    
        break
    x += 1
print(list)
'''
def prime_number(n):
    list=[]
    x=2
    cnt=0
    num=int(n)
    while (len(list)<n):
        flag=1
        for i in range(2,x):
            if x%i==0:
                flag=0
                break
            if flag==1:
                count=count+1
                list.append(x)
        if count==n:
            break
        x=x+1
    return list 
def main():
    n=int(input())
    output=prime_number(n)
    for i in range(0,n):
        print(output[i])
main()        
            
            