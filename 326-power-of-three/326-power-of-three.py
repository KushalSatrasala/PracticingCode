class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        if n == 0:
            return False
        
        while True:
            if i == n:
                return True
            if i > n:
                return False
            i *= 3