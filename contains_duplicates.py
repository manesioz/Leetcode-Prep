class Solution:
    #using built-in python data structures >>> 
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        if len(no_duplicates) < len(nums): 
            return True 
        else: 
            return False
        
