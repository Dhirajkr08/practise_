def reverse_list(arr,length):
    rev=0
    while n>0:
        i=n%10
        rev=rev*10+i
        n=n//10
    return rev    
def main():
    n=int(input()) 
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(reverse_list(arr,n))
main()        
           

