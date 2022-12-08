def find_maximumsum(arr,length):
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
        print(find_maximumsum(arr,n))
main()                           
