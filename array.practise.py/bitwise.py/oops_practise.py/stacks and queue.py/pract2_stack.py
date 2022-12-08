from typing import List


#========== User's Code Starts Here ==========

class MinStack:

    def __init__(self):
        self.stack=[]
        
    def push(self, val: int) -> None:
        self.stack.insert(0,val)
        
    def pop(self) -> None:
        temp=self.stack[0]
        del self.stack[0]
        return temp
        
    def top(self) -> int:
        return self.stack[0]
        
    def getMin(self) -> int:
        return min(self.stack)
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#========== User's Code Ends Here ==========


    
def main():
    stack=MinStack()
    while(True):
        operation=input()
        #cin>>operation;
        if(operation == "stop"):
            break
        elif(operation == "push"):
            ele=int(input())
            #cin>>ele;
            stack.push(ele)
            print("null")
        elif (operation == "pop"):
            stack.pop()
            print("null")
        
        elif (operation ==  "top"):
            x=stack.top()
            print(x)
        elif(operation == "min"):
            x=stack.getMin()
            print(x)
        
    
main()