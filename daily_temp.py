class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # exact same solution of the "next greater element" problem 
        # trick is to use a monotonic increasing stack 
        result = [0]*len(T) 
        stack = [] 
        for i, temp in enumerate(T): 
            while stack and temp > T[stack[-1]]: 
                result[stack[-1]] = i - stack[-1]  
                stack.pop() 
            stack.append(i) 
        return result
