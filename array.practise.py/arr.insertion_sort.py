def insertion_sort(arr,length):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]>arr[j-1]:
                d=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=d
    return arr                  

    
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        output=insertion_sort(arr,n)
    for i in range(n):
        print(output[i])
main()                            