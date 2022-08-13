class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mini_val = None
        
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                if mini_val is None or nums[low] < mini_val:
                    mini_val = nums[low]
                low = mid + 1
            else:
                if mini_val is None or nums[mid] < mini_val:
                    mini_val = nums[mid]
                high = mid - 1
        
        return mini_val
                