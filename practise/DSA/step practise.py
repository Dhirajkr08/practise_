def find_minimum(arr,length):
    mini=arr[0]
    for mini in arr:
        mini=min(arr)
    return mini
def find_maximum(arr,length):
    maxi=arr[0]  
    for maxi in arr:
        maxi=max(arr)
    return maxi
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print("maximum",find_maximum(arr,n))
        print("minimum",find_minimum(arr,n))
main()                      