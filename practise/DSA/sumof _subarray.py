'''def print_sum(arr,length):
    max_sum=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[k]
                if sum>max_sum:
                    max_sum=sum
    return max_sum
def main():
    n=int(input())
    arr=[]
    for i in range(len(arr)):
        arr.append(int(input()))
        print(print_sum(arr,n))
main()
'''

'''
def find_maximum(arr,length):
    max_sum=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[k]
                if sum>max_sum:
                    max_sum=sum
    return max_sum
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(find_maximum(arr,n))
main()  
'''


'''def find_maximum(arr,length):
    max_sum=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[j]
                if sum>max_sum:
                    max_sum=sum
    return max_sum
def main():
    n=int(input()) 
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(find_maximum(arr,n))
main()'''

'''
def find_maximum(arr,length):
    max_sum=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[k]
                if sum>max_sum:
                    max_sum=sum
    return max_sum
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input())) 
        print(find_maximum(arr,n))
main() 
'''

def find_maximum(arr,length):
    max_sum=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[k]
                if sum>max_sum:
                    max_sum=sum
    return max_sum
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))  
        print(find_maximum(arr,n))
main()                          
