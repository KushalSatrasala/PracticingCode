class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        def compare(x, y):
            if x[0] == y[0]:
                return y[1] - x[1]
            else:
                return x[0] - y[0]
        
        def find_max_beauty(sorted_list, value):
            low = 0
            high = len(sorted_list) - 1
            cur_max = 0  
            while low <= high:
                mid = int((low + high) / 2)
                if sorted_list[mid][0] == value:
                    return sorted_list[mid][1]
                else:
                    if value > sorted_list[mid][0]:
                        cur_max = sorted_list[mid][1]
                        low = mid + 1
                    else:
                        high = mid - 1
            return cur_max
    
        sorted_items = sorted(items, key=cmp_to_key(compare))
        list_len = len(sorted_items)
        
        i = 0
        cur_max = sorted_items[0][1]
        while i < list_len:     
            if sorted_items[i][1] > cur_max:
                cur_max = sorted_items[i][1]
            else:
                sorted_items[i][1] = cur_max
            i += 1
        res_list = list()
        for query in queries:
            res_list.append(find_max_beauty(sorted_items,query))
        
        return res_list