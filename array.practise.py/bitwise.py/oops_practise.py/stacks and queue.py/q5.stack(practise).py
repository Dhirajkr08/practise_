class solution:
    def validatestack(self,pushed:list[int],popped:list[int])->bool:
        stack=[]
        for i in pushed:
            stack.append(i) 
            while stack and popped and stack[-1]==popped[0]:
                stack.pop()
                popped.pop(0)
        return not stack             
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    n=int(input())
    arr1=[]
    for i in range(n):
        arr1.append(int(input()))
    s=solution()
    output=s.validatestack(arr,arr1)
    if output:
        print(True)
    else:
        print(False) 
main()           



