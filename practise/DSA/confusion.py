


"""def find_max(arr,length):
    maximum=arr[0]
    for maximum in arr:
        maximum=max(arr)
    return maximum
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(find_max(arr,n))
main()
"""

"""def find_minimum(arr,length):
    for minimum in arr:
        minimum=min(arr)
    return minimum
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(find_minimum(arr,n))
main()  
"""

"""def find_prime(n):
    x=2
    count=0
    num=str(n)
    list=[]
    while (len(list)<n):
        flag=1
        for i in range(2,x):
            if x%i==0:
                flag=0
                break
        if flag==1:
              count=count+1
              list.append(x)
        if count==n:
            break
        x=x+1
    return list    
def main():
    n=int(input())
    output=find_prime(n)
    for i in range(n):
        print(output[i])
main()                    
"""

#print n number of prime number
"""def find_prime(n):
    x=2
    count=0
    num=str(n)
    list=[]
    while (len(list)<n):
        flag=1
        for i in range(2,x):
            if x%i==0:
                flag=0
                break
        if flag==1:
            count=count+1
            list.append(x)
        if count==n:
            break
        x=x+1
    return list
def main():
    n=int(input())
    output=find_prime(n)
    for i in range(n):
        print(output[i])
main()  
"""

"""def print_subarray(arr,length):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print("",end="")
            for k in range(i,j+1):
                print(arr[k],end="")
            print()
def main():
    n=int(input())
    arr=[]
    for i in range(n): 
        arr.append(int(input()))
        print_subarray(arr,n)
    
main()    """

"""def print_subarray(arr,length):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print("",end="")
            for k in range(i,j+1):
                print(arr[k],end="")
            print()
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input())) 
        print_subarray(arr,n)
main() """ 

def find_maximumsum(arr,length):
    maxi=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[k]
                if sum>maxi:
                    maxi=sum
    return maxi
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_maximumsum(arr, n))
    
main()                    

