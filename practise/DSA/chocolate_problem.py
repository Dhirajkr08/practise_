from re import I
import sys
def find_mindiff(arr,n,m):
    if m==0 or n==0:
        return 0
    arr.sort()
    if n<m:
        return -1
    min_diff  =sys.maxsize
    first=0
    last=0
    i=0
    while (i+m-1<n):
        diff=arr[i+m-1]-arr[i]
        first=i
        last=i+m-1
    return(arr[last]-arr[first])
def main():
    n=int(input())
    arr=[]
    m=int(input())
    output=find_mindiff(arr,n,m) 
    for i in range(n):
        arr.append(int(input()))
        output=find_mindiff(arr,n,m)
    for i in range(n):
        print(output[i])     



main()