class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = dict()
        
        for ch in s:
            if ch not in char_dict:
                char_dict[ch] = 0
            char_dict[ch] += 1
        
        for ind, ch in enumerate(s):
            if char_dict[ch] == 1:
                return ind
        
        return -1