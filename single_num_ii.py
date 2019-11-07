from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int: #this solution is O(n) but uses O(n) extra space 
        d = defaultdict(list)
        for num in nums:
            d[num].append(num)
        return [key for key, val in d.items() if len(val) == 1][0]
