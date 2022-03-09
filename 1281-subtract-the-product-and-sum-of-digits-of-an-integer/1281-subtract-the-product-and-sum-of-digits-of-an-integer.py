class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        subAdd = 0
        
        if n == 0 :
            return 0
        
        while n:
            dig = n % 10
            prod = prod * dig 
            subAdd = subAdd + dig
            n = int(n / 10)
        
        return prod - subAdd