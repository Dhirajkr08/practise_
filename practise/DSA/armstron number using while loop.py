'''def find_armstrong(n):
    temp=n
    sum=0
    while temp>0:
        i=temp%10
        sum=sum+i**3
        temp=temp//10
    if n==sum:
        print("true")
    else:
        print("false") 
def main():
    n=int(input()) 
    find_armstrong(n)
main()                  '''


def print_armstrong(n):
    t=n
    sum=0
    while t>0:
        i=t%10
        sum=sum+i**3
        t=t//10
    if n==sum:
        print("true")
    else:
        print("false")
def main():
    n=int(input())
    print_armstrong(n)
main()                    
