#while loop
"""def find_series(n):
    i=1
    while i<=n:
        if i%5==0:
            i=i+1
            continue
        print(i)
        i=i+1
def main():
    n=int(input())
    find_series(n)
main()   """

# for loop
def find_series(n):
    for i in range(1,n+1):
        if i%5==0:
            continue
        print(i)
def main():
    n=int(input())
    find_series(n)
main()            