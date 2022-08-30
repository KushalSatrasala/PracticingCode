class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        
        res = ""
        while x:
            rem = x % 10
            x = x // 10
            res += str(rem)
        
        res = int(res)
        if neg:
            res *= -1
        
        if res < math.pow(-2, 31) or res > (math.pow(2, 31) - 1):
            return 0
        return res
            