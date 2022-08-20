class Solution:
    def compareDict(self, cur, t):
        for key in t.keys():
            if key not in cur:
                return False
            if t[key] > cur[key]:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        tlen = len(t)
        min_val = None
        min_str = None
        
        if tlen > slen:
            return ""
        
        t_dict = dict()
        cur_dict = dict()
        
        i = 0
        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 0
            t_dict[ch] += 1
        
        while i < slen and s[i] not in t_dict:
            i += 1
        
        j = slen - 1
        while j >= 0 and s[j] not in t_dict:
            j -= 1
        
        k = i
        while k <= j:
            if s[k] not in t_dict:
                k += 1
                continue
            
            if s[k] not in cur_dict:
                cur_dict[s[k]] = 0
            cur_dict[s[k]] += 1
            k += 1
            
            while i <= j:
                if (s[i] not in cur_dict) or (cur_dict[s[i]] > t_dict[s[i]]):
                    if s[i] in cur_dict:
                        cur_dict[s[i]] -= 1
                    i += 1
                    continue
                break
            
            flag = self.compareDict(cur_dict, t_dict)
            if flag:
                if min_val is None or (k - i) <= min_val:
                    min_val = k - i
                    min_str = s[i : k]

        if min_val is None:
            return ""
        else:
            return min_str
            
            
    
                
                