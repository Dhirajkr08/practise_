class solution:
    def validate(self,s:str)->bool:
        stack=[]
        dict={')':'(','}':'{',']':'['}
        for i in s:
            if i in dict.values():
                stack.append(i)
            else:
                if stack ==[] or stack.pop()!=dict[i]:
                    return False
        return stack==[]
def main():
    n=input()
    s=solution()
    output=s.validate(n)
    if output:
        print(True)
    else:
        print(False)
main()
                                

