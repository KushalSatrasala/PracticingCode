class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_indx = dict()
        for idx, num in enumerate(nums):
            if num not in num_indx:
                num_indx[num] = list()
            num_indx[num].append(idx)
        
        arrLen = len(nums)
        i = 0
        res_list = set()
        while i < arrLen:
            j = i + 1
            while j < arrLen:
                diff = 0 - (nums[i] + nums[j])
                if diff in num_indx:
                    for idx in num_indx[diff]:
                        if idx != i and idx != j:
                            tpl = tuple(sorted([nums[i], nums[j], nums[idx]]))
                            if tpl not in res_list:
                                res_list.add(tpl)
                            break
                j += 1
            i += 1
        
        return res_list
        