class Solution:
    def rob(self, nums: List[int]) -> int:
        slen = len(nums)
        
        if slen == 0:
            return 0
        if slen == 1:
            return nums[0]
        
        dp = [0  for _ in range(slen + 1)]
        dp[-1] = (0, 0)
        dp[-2] = (nums[-1], 0)
        dp[-3] = (0, nums[-2])
        i = slen - 3 
        while i >= 0:
            ne1_with_last, ne1_without_last = dp[i + 2]
            ne2_with_last, ne2_without_last = dp[i + 3]
            
            dp[i] = (max(ne1_with_last,ne2_with_last) + nums[i], max(ne1_without_last, ne2_without_last) + nums[i])
            i -= 1
        
        n1, n2 = dp[0]
        n3, n4 = dp[1]
        n5, n6 = dp[2]
        return max(n2, n3, n4, n5)   