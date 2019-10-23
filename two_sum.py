class Solution:
    #more efficient solution (O(n) runtime) 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} 
        for i in range(len(nums)): 
            if target - nums[i] in hash_table: 
                return [i, hash_table[target-nums[i]]]
            else: 
                hash_table[nums[i]] = i
        
    # sub-optimal solution (O(n^2)): 
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, first_num in enumerate(nums): 
    #         for j, next_num in enumerate(nums): 
    #             if i != j: 
    #                 if target - first_num == next_num: 
    #                     return [i, j]
    #                 else: 
    #                     continue 
        
