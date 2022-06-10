class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp_map = dict()
        s_len = len(nums)
        if k >= s_len:
            return sum(nums)
        
        def compute_the_average(nums, idx, k):
            if idx == s_len:
                return None
            if k == 1:
                return sum(nums[idx:]) / len(nums[idx:])
            
            if (idx, k) in dp_map:
                return dp_map[(idx, k)]
            
            max_val = 0
            i = idx
            cur_val = 0
            ct = 0
            while i < s_len - 1:
                ct += 1
                cur_val += nums[i]
                ret_val = compute_the_average(nums, i + 1, k - 1)
                if (cur_val / ct) + ret_val > max_val:
                    max_val = (cur_val / ct) + ret_val
                i += 1
            
            dp_map[(idx, k)] = max_val
            
            return max_val
        
        return(compute_the_average(nums, 0, k))