class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        num_indx = dict()
        for idx, num in enumerate(nums):
            num_indx[num] = idx
        
        arrLen = len(nums)
        i = 0
        res_list = set()
        while i < arrLen:
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            twoSum = -nums[i]
            for j in range(i+1,len(nums)):
                target = twoSum - nums[j]
                if target in num_indx and num_indx[target] > j:
                    res_list.add((-twoSum,nums[j],target))
                j += 1
            i += 1
        
        return res_list