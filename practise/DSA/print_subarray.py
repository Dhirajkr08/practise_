def print_subarray(arr,length):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print("",end="")
            for k in range(i,j+1):
                print(arr[k],end="")
            print()
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input())) 
        print_subarray(arr,n)
main()                       

