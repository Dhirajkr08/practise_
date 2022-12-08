def find_maximum(arr,length):
    max=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]>max:
                max=arr[j]
    return max
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(find_maximum(arr,n)) 
main()                       
