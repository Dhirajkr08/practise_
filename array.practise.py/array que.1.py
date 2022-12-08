def print_series(n):
    list=[]
    for i in range(1,n+1):
        list.append(i)
    return list
def main():
    n=int(input())
    output=(print_series(n))
    for i in range(n):
        print(output[i])
main()            
