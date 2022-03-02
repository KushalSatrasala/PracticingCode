class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = int((high - low) / 2)
        if (low % 2) == 1:
           return res + 1
        elif (low % 2) == 0 and (high % 2) == 1:
            return res + 1
        return res
        
        