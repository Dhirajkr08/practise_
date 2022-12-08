'''class solution:
    def removeDuplicates(self,s:str)->str:
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
def main():
    n=input()
    s=solution()
    output=s.removeDuplicates(n)
    print(output)
main()
''' 

# validate stack
class solution:
    def validateStack(self,pushed:list[int],popped:list[int])->int:
        stack=[]
        for i in pushed:
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
    output=s.validateStack(arr,arr1)
    if output:
        print(True) 
    else:
        print(False)
main()               





