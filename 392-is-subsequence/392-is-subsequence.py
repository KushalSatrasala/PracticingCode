class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        t_len = len(t)
        s_len = len(s)
        
        if s_len > t_len:
            return False
        
        for ch in s:
            while i < t_len and t[i] != ch: 
                i += 1
            if i == t_len:
                return False    
            i = i + 1
        
        return True
        