class Solution:
    def minInsertions(self, s: str) -> int:
        res_add = 0
        s_len = len(s)
        
        i = 0
        ob = 0
        cb = 0
        while i < s_len:
            if s[i] == "(":
                ob += 1
                i += 1
            elif s[i] == ")":
                cb = 0
                while i < s_len and s[i] == ")":
                    cb += 1
                    i += 1
                if cb % 2 == 1:
                    res_add += 1
                    cb += 1
                cb = cb // 2
                if cb == ob:
                    cb = 0
                    ob = 0
                    continue
                elif cb > ob:
                    res_add += cb - ob
                    ob = 0
                    cb = 0
                else:
                    ob = ob - cb
                    cb = 0
        
        res_add += ob * 2
        res_add += cb // 2
        return res_add