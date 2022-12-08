class Solution:
    def nextGreaterElements(self, nums: list[int])-> list[int]:
        stack=[]
        size=len(nums)
        nums=nums+nums
        res=[-1]*size
        for i in list(range(size))*2:
            while stack and stack[-1]<nums[i]:
                res[stack.pop()]=nums[i]
            stack.append(i)
        return res
                





   
    
    
    
    
    
def main():
    n=int(input())
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    s=Solution()
    output = s.nextGreaterElements(arr)
    string =""
    for i in range(0,n):
        string =string + str(output[i]) +" "
    print(string)
    
main()