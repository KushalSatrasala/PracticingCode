class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        a,b = 0,1
        for i in range(n-1):
            result = a+b
            a = b
            b = result
        return result