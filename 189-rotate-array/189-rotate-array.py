class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr_len = len(nums)
        k = k % arr_len
        
        if (arr_len - k) > k:
            temp_list = list()
            i = arr_len - 1
            l = 0
            while l < k:
                temp_list.append(nums[i])
                i -= 1
                l += 1

            j = arr_len - 1
            while i >= 0:
                nums[j] = nums[i]
                j -= 1
                i -= 1
            
            l = 0
            while j >= 0:
                nums[j] = temp_list[l]
                j -= 1
                l += 1
        else:
            temp_list = list()
            i = 0
            while i < (arr_len - k):
                temp_list.append(nums[i])
                i += 1

            j = 0
            while i < arr_len:
                nums[j] = nums[i]
                j += 1
                i += 1
            
            l = 0
            while j < arr_len:
                nums[j] = temp_list[l]
                j += 1
                l += 1