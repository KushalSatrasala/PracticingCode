class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        i = 0 
        arr_len = len(nums)
        while i < arr_len and nums[i] < 0:
            i += 1
        
        left = i - 1
        right = i 
        res_arr = list()

        while left >= 0 and right < arr_len:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            
            if left_sq < right_sq:
                res_arr.append(left_sq)
                left -= 1
            else:
                res_arr.append(right_sq)
                right += 1
        
        while left >=0 :
            left_sq = nums[left] * nums[left]
            res_arr.append(left_sq)
            left -= 1
        
        while right < arr_len :
            right_sq = nums[right] * nums[right]
            res_arr.append(right_sq)
            right += 1
        
        return res_arr