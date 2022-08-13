class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_res = None
        cur_prod = None
        i = 0
        slen = len(nums)
        start = 0
        
        while i < slen:
            if nums[i] == 0:
                if max_res is None or 0 > max_res:
                    max_res = 0
                if cur_prod is not None and cur_prod < 0:
                    j = start 
                    while j < i and cur_prod < 0:
                        cur_prod = cur_prod // nums[j]
                        if cur_prod > 0 and j + 1 == i:
                            cur_prod = None 
                            break
                        j += 1
                if max_res is None or (cur_prod is not None and cur_prod > max_res):
                    max_res = cur_prod
                cur_prod = None
                start = i + 1
                i += 1
            else:
                if cur_prod is None:
                    cur_prod = nums[i]
                else:
                    cur_prod *= nums[i]
                if max_res is None or (cur_prod is not None and cur_prod > max_res):
                    max_res = cur_prod
                i += 1
            
        if cur_prod is not None and cur_prod < 0:
            j = start 
            while j < i and cur_prod < 0:
                cur_prod = cur_prod // nums[j]
                if cur_prod > 0 and j + 1 == i:
                    cur_prod = None 
                    break
                j += 1
            if max_res is None or (cur_prod is not None and cur_prod > max_res):
                max_res = cur_prod
        
        return max_res
            