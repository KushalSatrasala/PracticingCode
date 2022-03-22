class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        leftProd = [0 for _ in range(numLen)]
        rightProd = [0 for _ in range(numLen)]
        resList = list()
        
        i = 0
        curProd = 1
        while i < numLen:
            leftProd[i] = curProd
            curProd *= nums[i]
            i += 1
        
        i = numLen - 1
        curProd = 1
        while i >= 0:
            rightProd[i] = curProd
            curProd *= nums[i]
            i -= 1
        
        i = 0
        while i < numLen:
            resList.append(leftProd[i] * rightProd[i])
            i += 1
        
        return resList