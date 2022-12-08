'''def store_prime(n):
    num=str(n)
    count=0
    x=2
    list=[]
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
        return
    x=x+1
    return list
def main():
    n=int(input())
    output=store_prime(n)
    for i in range(0,n):
        print(output[i])

main()
'''

'''def prime_number(n):
    list=[]
    x=2
    count=0
    num=str(n)
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

'''

'''def store_prime(n):
    list=[]
    x=2
    count=0
    num=str(n)
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
    output=store_prime(n) 
    for i in range(n):
        print(output[i])
main() 
'''

'''def find_prime(n):
    list=[]
    x=2
    c=0
    num=str(n)
    while (len(list)<n):
        flag=1
        for i in range(2,x):
            if x%i==0:
                flag=0
                break
        if flag==1:
            c=c+1
            list.append(x)
        if c==n:
            break
        x=x+1
    return list
def main():
    n=int(input())
    output=find_prime(n)
    for i in range(n):
        print(output[i]) 
main()  '''

def print_prime(n):
    list=[]
    x=2
    count=0
    num=str(n)
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
    output=print_prime(n)
    for i in range(n):
        print(output[i])
main()        





