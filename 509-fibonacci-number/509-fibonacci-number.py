class Solution:
    def fib(self, n: int) -> int:
        res_list = list()
        res_list.append(0)
        res_list.append(1)
        
        i = 2
        while i <= n:
            res_list.append(res_list[i - 1] + res_list[i - 2])
            i += 1
        
        return res_list[n]