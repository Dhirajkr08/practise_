def print_numbers(n,m):
    for i in range(1,n):
        if i==m:
            break
        print(i)
def main():
    n=int(input())
    m=int(input())
    print_numbers(n,m)
main()            
