class solution:
    def findDuplicates(self,s:str)->str:
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
    output=s.findDuplicates(n)
    print(output)
main()                        