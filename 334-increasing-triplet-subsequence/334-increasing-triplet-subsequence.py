class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        nlen = len(nums)
        if nlen < 3:
            return False
        
        firstMin = max(nums) + 1
        secMin = max(nums) + 1

        i = 0
        while i < nlen:
            if nums[i] < firstMin:
                firstMin = nums[i]
            if (nums[i] > firstMin) :
                secMin = min(nums[i], secMin);
            if nums[i] > secMin:
                return True
            i += 1

        return False