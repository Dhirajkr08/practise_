def find_largest(a,b,c):
    if a>b and a>c:
        print(a)
    if b>a and b>c:
        print(b)
    else:
        print(c)
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    find_largest(a,b,c)
main()
                    