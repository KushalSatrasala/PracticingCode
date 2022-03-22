class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalCount = 0
        numLen = len(nums)
        i = 0
        res = 0
        curSum = 0
        prevSum = defaultdict(lambda : 0)
        
        while i < numLen:
            curSum += nums[i]

            if curSum == k: 
                res += 1        

            if (curSum - k) in prevSum:
                res += prevSum[curSum - k]
           
            prevSum[curSum] += 1
            
            i += 1
      
        return res
            