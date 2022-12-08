def decimal_binary(n):
    if n>=1:
        decimal_binary(n//2)
        print(n%2,end='')
def main():
    n=int(input("enter the number =") )  
    decimal_binary(n)
main()                  