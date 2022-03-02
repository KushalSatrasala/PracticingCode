class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return int((high - low + low%2 + high%2) /2)
        
        