class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        i = 3
        while i <= n:
            res = a + b + c
            a = b
            b = c
            c = res
            
            i += 1
        
        return res