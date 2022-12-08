class solution:
    def isvalid(self,s:str)->bool:
        stack=[]
        val={']':'[',')':'(','}':'{'} 
        for i in s:
            if i in val.values():
                stack.append(i)
            else:
                if stack==[] or stack.pop()!=val[i] :
                    return False
        return stack==[]                                       
def main():
    n=input()
    s=solution()
    output=s.isvalid(n)
    if output:
        print(True)
    else:
        print(False)
main()                                   