class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        slen = len(prices)
        if slen == 1:
            return 0
        
        i = 0
        while True:
            while i + 1 < slen and prices[i] >= prices[i + 1]:
                i += 1
            if i + 1 == slen:
                break
            buy = prices[i]
            while i + 1 < slen and prices[i] < prices[i + 1]:
                i += 1
            if i + 1 == slen:
                if prices[i] > buy:
                    max_profit += prices[i] - buy
                break
            max_profit += prices[i] - buy
        
        return max_profit