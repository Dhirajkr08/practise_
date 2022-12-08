def sort_array(arr,length):
    for i in range(len(arr)-1):
        m=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[m]:
                m=j
        d=arr[i]
        arr[i]=arr[m]
        arr[m]=d        

            
    return arr
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        output=sort_array(arr,n)
    for i in range(n):
        print(output[i])
main()                        
