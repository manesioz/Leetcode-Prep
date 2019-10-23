class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 1: 
            prod = 1 
            for num in nums: 
                if num != 0: 
                    prod *= num
            return [0 if num != 0 else prod for num in nums]
        elif nums.count(0) > 1: 
            return [0]*len(nums)
        else: 
            prod = 1 
            for num in nums: 
                prod *= num 
            return [int(prod/num) for num in nums] 
