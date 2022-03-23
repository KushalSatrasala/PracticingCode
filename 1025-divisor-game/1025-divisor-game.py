class Solution:
    def divisorGame(self, n: int) -> bool:
        dp_map = [False for _ in range( n+1 )]
        dp_map[1] = False
        i = 2
        while i <= n:
            j = 1
            while j < i:
                if i % j == 0 and not dp_map[i - j]:
                    dp_map[i] = True
                    break
                j += 1
            i += 1
        return dp_map[n]
        