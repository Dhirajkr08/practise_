class solution:
    def trap(self,heights:list[int])->int:
        left=0
        right=len(heights)-1
        left_max=heights[left]
        right_max=heights[right]
        result=0
        while left<right:
            if left_max<right_max:
                left=left+1
                left_max=max(left_max,heights[left])
                result=result+left_max-heights[left]
            else:
                right_max=max(right_max,heights[right]) 
                result=result+right_max-heights[right]
        return result           
        
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    s=solution()
    output=s.trap(arr)
    print(output)
main()                           


   