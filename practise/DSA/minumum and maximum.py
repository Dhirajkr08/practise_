"""
def find_maximum(arr,length):
    for maximum in arr:
        maximum=max(arr)
    return maximum 
def find_minimum(arr,length):
    for minimum in arr:
        minimum=min(arr) 
    return minimum
def main():
    n=int(input())
    arr=[]
    sum=0
    for i in range(n):
        arr.append(int(input()))
        print(find_maximum(arr,n)) 
        print(find_minimum(arr,n))
        sum=find_minimum(arr,n)+find_maximum(arr,n)
        print(sum)
main()                     """


def find_minimum(arr,length):
    for i in range(len(arr)):
        i=min(arr)
    return i
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        print(find_minimum(arr,n))
main()                