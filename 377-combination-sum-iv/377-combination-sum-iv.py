class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        i = 1
        while i <= target:
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
            i += 1
        return dp[target]