def find_series(n):
    for i in range(1,n+1):
        if i*i*i<=n:
            print(i*i*i)
def main():
    n=int(input())
    find_series(n)
main()                