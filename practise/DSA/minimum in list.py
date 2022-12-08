def print_minimum(arr,length):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]>min:
            min=arr[i]
    return min
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(print_minimum(arr,n))
main()                    