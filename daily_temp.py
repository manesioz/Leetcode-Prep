class Solution:
    # def dailyTemperatures(self, T: List[int]) -> List[int]: #sub-optimal, O(n^2)
    #     output = [] 
    #     for i, outer_num in enumerate(T): 
    #         for j, inner_num in enumerate(T): 
    #             if inner_num > outer_num and j > i: 
    #                 output.append(j-i)
    #                 break
    #         if len(output) < len(T[:i+1]): 
    #             output.append(0)
    #     return output 
    def dailyTemperatures(self, T: List[int]) -> List[int]: #solution using a stack, O(n) runtime 
        stack = []
        wait = [0]*len(T)
        for i, temp in enumerate(T): 
            while len(stack) > 0 and T[stack[-1]] < temp: 
                j = stack.pop()
                wait[j] = i-j
            stack.append(i)
        return wait
