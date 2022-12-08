def print_pattern(n):
    i=1
    while i<=n:
        j=n
        while j>=i:
            print("*",end="")
            j=j-1
        print()
        i=i+1
    i=1
    while i<=n:
        j=1
        while j<=i:
            print("*",end="")
            j=j+1
        print()
        i=i+1
def main():
    n=int(input())
    print_pattern(n)
main()                        
   