class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = n * -1
            x =  1 / x
        
        def multiple(a, i):
            if i == 0:
                return 1
            elif i % 2 == 0:
                return multiple(a * a, i // 2)
            else:
                return a * multiple(a * a, i // 2)

        return multiple(x, n)