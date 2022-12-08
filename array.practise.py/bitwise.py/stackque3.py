'''Given two integer arrays pushed and popped each with distinct values, 
return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, 
or false otherwise.'''
class solution:
    def validateSequence(self,pushed:list[int],popped:list[int])->int:
        stack=[]
        for i in pushed:
            stack.append(i)
            while popped and stack and stack[-1]==popped[0]:
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
    output=s.validateSequence(arr,arr1)
    if output:
        print(True) 
    else:
        print(False) 
main()                                 