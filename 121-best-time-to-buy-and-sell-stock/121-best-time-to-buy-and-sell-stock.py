class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        max_ret = 0
        i = len(prices) - 1

        if i == 0:
            return 0

        while i >= 0:
            if max_val - prices[i] > max_ret:
                max_ret = max_val - prices[i]
            elif prices[i] > max_val:
                max_val = prices[i]   
            i -= 1
        
        return max_ret
            
            
        