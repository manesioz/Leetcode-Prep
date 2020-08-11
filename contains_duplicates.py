class Solution:
    #using built-in python data structures >>> 
    def containsDuplicate(self, nums: List[int]) -> bool: 
        return len(nums) != len(set(nums)) 
