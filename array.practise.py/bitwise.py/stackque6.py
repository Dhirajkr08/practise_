'''Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array,
 which means you could search circularly to find its next greater number. If it doesn't exist,
  return -1 for this number.'''

class solution:
    def nextGreaterElement(self,nums:list[int])->int:
        size=len(nums)
        nums=nums+nums
        res=[-1]*size
        stack=[]
        for i in list(range(size))*2:
            while stack and (nums[stack[-1]]<nums[i]):
                res[stack.pop()]=stack[i]
            stack.append(i)
        return res        
def main():
    n=int(input())
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    s=solution()
    output = s.nextGreaterElement(arr)
    string =""
    for i in range(0,n):
        string =string + str(output[i]) +" "
    print(string)
    
main()               

