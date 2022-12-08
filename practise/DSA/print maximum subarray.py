


def print_maximum(arr,length):
    maximum_sum=0
    for i in range(length):
        for j in range(i,length):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[k]
                if sum>maximum_sum:
                    maximum_sum=sum
    return maximum_sum                 
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(print_maximum(arr, n))