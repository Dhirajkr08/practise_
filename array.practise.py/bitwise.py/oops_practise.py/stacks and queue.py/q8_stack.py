class solution:
    def __init__(self):
        self.stack=[]
    def next(self,price:int)->int:
        span=1
        while self.stack and self.stack[-1][0]<=price :
            span=span+self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        return span
def main():
    n=int(input())
    arr=[]
    s=solution()
    for i in range(n):
        print(s.next(int(input())))
main()        
