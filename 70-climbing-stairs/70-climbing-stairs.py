class Solution:
    def climbStairs(self, n: int) -> int:
        dp_map = [None for _ in range(n + 1)]
        
        if n == 1:
            return 1
        
        dp_map[0] = 0
        dp_map[1] = 1
        dp_map[2] = 2
        
        i = 3
        while i <= n:
            dp_map[i] = dp_map[i - 1] + dp_map[i - 2]
            i += 1
        
        return dp_map[n]
        