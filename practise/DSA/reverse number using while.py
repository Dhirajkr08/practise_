"""def reverse(n):
    rev=0
    while n>0:
        i=n%10
        rev=rev*10+i
        n=n//10
    
    return rev 
def main():
    n=int(input()) 
    print(reverse(n))
main()  
"""

def print_reverse(n):
    rev=0
    while n>0:
        i=n%10
        rev=rev*10+i
        n=n//10
    return rev
def main():
    n=int(input())
    print(print_reverse(n))
main()            
