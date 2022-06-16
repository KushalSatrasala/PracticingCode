class Solution:
    def return_palindrom(self, s, left, right):
        s_len = len(s)
        l = left
        j = right
        while (l >= 0 ) and ( j < s_len) and (s[l] == s[j]):
            l -= 1
            j += 1
        return l + 1, j - 1
        
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        max_len = 1
        max_len_indices = (0,0)

        i = 0
        while i < s_len:
            pal_start, pal_end = self.return_palindrom(s, i - 1, i + 1)
            if (pal_end + 1 - pal_start) > max_len:
                max_len = (pal_end + 1 - pal_start)
                max_len_indices = (pal_start, pal_end)
            
            if i + 1 < s_len and s[i] == s[i+1]:
                pal_start, pal_end = self.return_palindrom(s, i - 1, i + 2)
                if (pal_end + 1 - pal_start) > max_len:
                    max_len = (pal_end + 1 - pal_start)
                    max_len_indices = (pal_start, pal_end)
            i = i + 1
        
        res_i, res_j = max_len_indices
        return s[res_i: res_j + 1]
                