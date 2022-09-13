class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        slen = len(heights)
        max_val = heights[slen - 1]
        i = slen - 2
        res_list = list()
        res_list.append(slen - 1)
        while i >= 0:
            if heights[i] > max_val:
                res_list.append(i)
                max_val = heights[i]
            
            i -= 1
        
        return res_list[::-1]
            