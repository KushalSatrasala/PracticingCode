class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        arrLen = len(nums)
        
        return nums[int(arrLen / 2)]