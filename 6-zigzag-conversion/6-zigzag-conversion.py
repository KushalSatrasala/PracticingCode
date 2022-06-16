class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res_mat = [list() for i in range(numRows)]
        ch = 0
        s_len = len(s)
        i = 0
        while True:
            while ch < s_len and i < numRows - 1:
                res_mat[i].append(s[ch])
                i += 1
                ch += 1
            if ch == s_len:
                break
            
            while ch < s_len and i > 0:
                res_mat[i].append(s[ch])
                i -= 1
                ch += 1
                
            if ch == s_len:
                break
        
        res_str = ""
        for lt in res_mat:
            res_str += "".join(lt)
            
        return res_str
        