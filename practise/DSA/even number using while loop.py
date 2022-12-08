"""def find_even(n):
    i=1
    while (i<=n):
        if i%2==0:
            print(i)
        i=i+1
def main():
    n=int(input())
    find_even(n)
main()            """


#using for loop
def find_even(n):
    for i in range(2,n+1):
        if i%2==0:
            print(i)

def main():
    n=int(input())
    find_even(n)
main()                