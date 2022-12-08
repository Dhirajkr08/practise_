def print_pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()    
def main():
    n=int(input())
    print_pattern(n)
main()                