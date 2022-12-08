class solution:
    def removeduplicates(self,s:str)-> str:
        stack=[]
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)            
def main():
    n="azxxzy"
    s=solution()
    output=s.removeduplicates(n)
    print(output)
main()                        
