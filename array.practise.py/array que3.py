def find_minimum(arr,length):
    min=arr[0]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]<min:
                min=arr[j]
    return min
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(find_minimum(arr,n))
main()                        
