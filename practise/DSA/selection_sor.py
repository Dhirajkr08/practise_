'''def sort_array(arr,length):
    for i in range(len(arr)):
        c=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[c]:
                c=j
        d=arr[i]
        arr[i]=arr[c]
        arr[c]=d
    return arr  
def main():
    n=int(input())
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    output = sort_array(arr,n)
    for i in range(0,n):
        print(output[i])
    
main() '''


'''def print_array(arr,length):
    for i in range(len(arr)):
        c=i
        for j in range(i+1,len(arr)):
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
        output=print_array(arr,n)
    for i in range(n):
        print(output[i])
main() '''

'''def print_array(arr,length):
    for i in range(len(arr)):
        c=i
        for j in range(i+1,len(arr)):
            
            if arr[i]>arr[c]:
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
        output=print_array(arr,n)
    for i in range(n):
        print(output[i])
main()  '''

def sort_array(arr,length):
    for i in range(len(arr)):
        c=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[c]:
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
        output=sort_array(arr,n) 
    for i in range(n):
        print(output[i])
main()                           
