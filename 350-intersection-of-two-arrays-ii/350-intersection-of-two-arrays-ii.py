class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_map = dict()
        
        for num in nums1:
            if num not in dict_map:
                dict_map[num] = 0
            dict_map[num] += 1
        
        res_list = list()
        
        for num in nums2:
            if num in dict_map and dict_map[num] > 0:
                res_list.append(num)
                dict_map[num] -= 1
        
        return res_list