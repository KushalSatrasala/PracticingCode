class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        
        if top == 1:
            return cost[0]
        
        if top == 2:
            return min(cost[0], cost[1])
        
        dp_map = [None for _ in range(top)]
        
        i = top - 1
        dp_map[i] = cost[i]
        i = i - 1
        dp_map[i] = min(cost[i], cost[i] + cost[i + 1])
        i = i - 1
        while i >= 0:
            dp_map[i] = min(cost[i]+dp_map[i + 1], cost[i]+dp_map[i + 2])
            i -= 1
        return min(dp_map[0], dp_map[1])