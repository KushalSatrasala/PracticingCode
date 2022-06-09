class Solution:
    def minInsertions(self, s: str) -> int:
        res_add = 0
        s_len = len(s)
        i = 0
        cb = 0
        while i < s_len and s[i] == ")":
            cb += 1
            i += 1

        res_add += int(cb / 2)
        if cb % 2 == 1:
            res_add += 2
        
        j = s_len - 1
        op = 0
        while j >= 0 and s[j] == "(":
            op += 1
            j -= 1
        res_add += op * 2
        
        
        ob = 0
        cb = 0
        while i < s_len and i <= j:
            if s[i] == "(":
                ob += 1
                i += 1
            elif s[i] == ")":
                cb = 0
                while i < s_len and s[i] == ")":
                    cb += 1
                    i += 1
                print(ob, cb)
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