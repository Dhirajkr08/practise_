def sort_number(arr,length):
    for i in range(len(arr)):
        c=i
        for j in range(i,len(arr)):
            if arr[j]>arr[c]:
                c=j
        d=arr[i]
        arr[i]=arr[c]
        arr[c]=d
    return arr
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        output=sort_number(arr,n)
    for i in range(n):
        print(output[i])
main()        
                            