def find_odd(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
def main():
    n=int(input())
    find_odd(n)
main()            
