'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type'''

class solution:
    def isvalid(self,s:str)->bool:
        stack=[]
        dict={'}':'{',']':'[',')':'('}
        for i in s:
            if i in dict.values():
                stack.append(i)
            else:
                if stack==[] or stack.pop()!=dict[i]:
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