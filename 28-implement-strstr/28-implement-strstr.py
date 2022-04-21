class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        all_start_indices = list()
        h_len = len(haystack)
        n_len = len(needle)
        
        i = 0
        while i < h_len:
            if haystack[i] == needle[0]:
                all_start_indices.append(i)
            i += 1
        
        for start in all_start_indices:
            i = 0
            found = True
            while (start + i) < h_len and i < n_len:
                if haystack[start + i] != needle[i]:
                    found = False
                    break
                i += 1
            
            if found and i == n_len:
                return start
        
        return -1