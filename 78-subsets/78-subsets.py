class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res_list = list()
        res_list.append([])
        
        for num in nums:
            i = 0
            llen = len(res_list)
            while i < llen:
                cur_list = copy.deepcopy(res_list[i])
                cur_list.append(num)
                res_list.append(cur_list)
                i += 1
        
        return res_list
        