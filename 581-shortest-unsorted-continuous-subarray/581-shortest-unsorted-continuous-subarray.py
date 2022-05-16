class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n_len = len(nums)
        i = 0
        
        if n_len == 0:
            return 0
        
        sorted_arr = sorted(nums)
        rem_val = 0
        while i < n_len and nums[i] == sorted_arr[i]:
            i += 1
            rem_val += 1
        
        j = n_len - 1
        
        if i == n_len:
            return 0
        
        while j > 0 and nums[j] == sorted_arr[j]:
            rem_val += 1
            j -= 1
        
        return (n_len - rem_val)