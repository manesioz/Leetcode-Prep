class Solution:
    '''
    This solution utilizes the monotonic stack (https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step)
    
    The key insights is that the answer is sum(A[i]*left[i]*right[i]), where `left` is the previous less elements and `right` is the next less elements. 
    
    '''
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = (10**9) + 7
        
        leftLeast = self.lastLeastElem(A)
        rightLeast = self.nextLeastElem(A) 
        
        numbersToSum = [elem*left*right for elem, left, right in zip(A, leftLeast, rightLeast)] 
        return sum(numbersToSum)%mod

    def lastLeastElem(self, A: List[int]) -> List[int]: 
        result = [-1]*len(A) 
        stack = [] 
        
        for i, num in enumerate(A): 
            while stack and num < A[stack[-1]]: 
                stack.pop() 
            result[i] = stack[-1] if stack else -1 
            stack.append(i)
            
        for i, _ in enumerate(A): 
            result[i] =  i+1 if result[i] == -1 else i - result[i]
            
        return result
    
    def nextLeastElem(self, A: List[int]) -> List[int]: 
        result = [-1]*len(A) 
        stack = [] 
        
        for i, num in enumerate(A): 
            while stack and num < A[stack[-1]]: 
                result[stack[-1]] = i 
                stack.pop() 
            stack.append(i)
            
        for i, _ in enumerate(A): 
            result[i] =  result[i] =  len(A) - i if result[i] == -1 else result[i] - i
            
        return result 
