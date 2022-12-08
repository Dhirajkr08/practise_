"""def find_series(n):
    i=1
    while i*i<=n:
        print(i*i)
        i=i+1 
def main():
    n=int(input())
    find_series(n)
main()       """

#using for loop
def find_series(n):
    for i in range(1,n):
        if i*i<=n:
            print(i*i)
def main():
    n=int(input())
    find_series(n)
main()                
