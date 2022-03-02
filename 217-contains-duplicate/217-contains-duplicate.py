class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = dict()
        
        for num in nums:
            if num in dups:
                return True
            dups[num] = 1
        return False