def print_even(n):
    for i in range(1,n+1):
        if i%4==0:
            continue
        if i%2==0:
            print(i)
def main():
    n=int(input())
    print_even(n)
main()                