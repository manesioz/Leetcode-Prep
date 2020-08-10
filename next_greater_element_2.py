class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)
        stack = []
        n = len(nums)
        for i in range(2*n): 
            while stack and nums[stack[-1]] < nums[i%n]: 
                result[stack[-1]] = nums[i%n]
                stack.pop() 
            stack.append(i%n)
            
        return result
            

# push when top element is greater than element about to be pushed, or if stack empty
# pop if top element is less than current element. continue until it isn't. 
# for each element popped, you know its NGE is the element you're about to push ("num")

#note: since it is a circular array, double the size and modulo the index 

#nums: [5, 3, 2, 10, 6, 8, 1, 4, 12, 7, 4]
#stack: [8]
#result: [10, 10, 10, 12, 12, 12, 12, 12, -1, -1, -1]
