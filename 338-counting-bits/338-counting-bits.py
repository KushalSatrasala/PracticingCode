class Solution:
    def countBits(self, n: int) -> List[int]:
        res_list = list()
        res_list.append(0)
        prev_rest = 0
        next_reset = 1
        cur_count = 0
        i = 1
        while i <= n:
            if i == next_reset:
                res_list.append(1)
                prev_reset = next_reset
                next_reset *= 2
            else:
                res_list.append(1 + res_list[i - prev_reset])
            
            i += 1
        
        return res_list
            