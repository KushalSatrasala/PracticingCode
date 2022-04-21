class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n_len = len(nums)
        if n_len == 1 or n_len == 0:
            return n_len

        i = 0
        j = 0
        while j < n_len:
            nums[i] = nums[j]
            while j < n_len and nums[i] == nums[j]:
                j += 1
            i += 1
        
        return i