class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = dict()
        i = 0
        slen = len(s)
        ch_dict = dict()
        max_ch = 0
        max_val = 0
        
        start = 0
        while i < slen:
            if s[i] not in ch_dict:
                ch_dict[s[i]] = 0
            ch_dict[s[i]] += 1
            
            max_ch = max(max_ch, ch_dict[s[i]])
            while (i - start + 1- max_ch > k):
                ch_dict[s[start]] -= 1
                start += 1
            
            if i - start + 1 > max_val:
                max_val = i - start + 1
            
            i += 1
        
        return max_val
            
    