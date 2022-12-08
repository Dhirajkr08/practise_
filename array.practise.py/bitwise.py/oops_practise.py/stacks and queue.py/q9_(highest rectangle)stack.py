class solution:
    def islargestrectanglearea(self,heights:list[int])->int:
        heights.append(0)
        stack=[-1]
        ans=0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                height=heights[stack.pop()]
                width=i-stack[-1]-1
                ans=max(ans,height*width)
            stack.append(i)
        return ans        
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    s=solution()
    output=s.islargestrectanglearea(arr)
    print(output)
main()                     


