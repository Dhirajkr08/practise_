def find_prime(n):
    x=2
    arr=[]
    num=str(n)
    count=0
    while len(arr)<n:
        flag=1
        for i in range(2,x):
            if x%i==0:
                flag=0
                break
        if flag==1:
            count=count+1
            arr.append(x)
        if count==n:
            break
        x=x+1
    return arr
def main():
    n=int(input("how many prime number:"))
    output=find_prime(n)
    for i in range(n):
        print(output[i])
main()                
