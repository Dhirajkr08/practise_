#print prime number till nTh number of times
"""
def find_primeno(n):
    list=[]
    flag=1
    for i in range(2,n*n):
        for j in range(2,i):
            if i%j==0:
                flag=0
                break
        if flag==1:
            list.append(i)
    return list
def main():
    n=int(input())
    output=find_primeno(n)
    for i in range(0,n):
        print(output[i])                
"""

#print sum of subarray
"""def print_subarray(arr, length):
    for i in range(0,len(arr)):
        for j in range (i,len(arr)):
            sum=0
            for k in range(i,j+1):
                
                sum=sum+arr[k]
                if sum>max_sum:
                    max_sum=sum
    return max_sum                     
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print_subarray(arr, n)
    
main()

"""

def find_primeno(n):
    list=[]
    for i in range(2,n*n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            list.append(i)
    return list
    
    

def main():
    n=int(input())
    output=find_primeno(n)
    for i in range(0,n):
        print(output[i])     