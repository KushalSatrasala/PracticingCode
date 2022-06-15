class Solution:
    def compare_strs(self, str1, str2):
        s1_len = len(str1)
        s2_len = len(str2)
        if abs(s1_len - s2_len) > 1 or s1_len == s2_len:
            return False
        else:
            diff = 0
            i = 0
            j = 0
            while i < s1_len and j < s2_len:
                if str1[i] != str2[j]:
                    diff += 1
                    if s1_len > s2_len:
                        i += 1
                    elif s2_len > s1_len:
                        j += 1
                    else:
                        return False
                else:
                    i += 1
                    j += 1
                if diff > 1:
                    return False
            
            return True
    
    def compare(self, s1,s2):
        return len(s1) - len(s2)

    def longestStrChain(self, words: List[str]) -> int:        
        dp_map = dict()
        sorted_arr = sorted(words, key = cmp_to_key(self.compare))
        s_len = len(sorted_arr)

        def compute_chain(idx, sorted_arr):
            if idx == s_len:
                return 0
            if idx in dp_map:
                return dp_map[idx]
            maxi = 0
            i = idx + 1
            while i < s_len:
                if self.compare_strs(sorted_arr[idx], sorted_arr[i]):
                    ret = compute_chain(i,sorted_arr)
                    if ret > maxi:
                        maxi = ret
                i += 1            
            dp_map[idx] = max(1, 1 + maxi)
            return dp_map[idx]
        
        i = 0 
        while i < s_len:
            if i not in dp_map:
                compute_chain(i, sorted_arr)
            i += 1
        return max(list(dp_map.values()))
        