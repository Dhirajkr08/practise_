def store_number(n):
    array=[]
    for i in range(1,n+1):
        array.append(i)
    return array
def main():
    n=int(input())        
    output=store_number(n)
    for i in range(0,n):
        print(output[i])
main()        
