class Solution:
    def canJump(self, nums: List[int]) -> bool:
        slen = len(nums)
        dp = [False for _ in range(slen)]
        dp[-1] = True
        last = slen - 1
        i = slen - 2
        
        while i >= 0:
            if i + nums[i] >= last:
                last = i
            i -= 1
        
        if last <= 0:
            return True
        return False
                
                