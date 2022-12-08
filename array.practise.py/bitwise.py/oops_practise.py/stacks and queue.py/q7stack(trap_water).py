class solution:
    def trap(self,height:list[int])->int:
        left=0
        right=len(height)-1
        left_max=height[left]
        right_max=height[right]
        result=0
        while left<right:
            if left_max<right_max:
                left=left+1
                left_max=max(left_max,height[left])
                result=result+left_max-height[left]
            else:
                right=right-1
                right_max=max(right_max,height[right])
                result=result+right_max-height[right]
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
