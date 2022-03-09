class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        def compare_char_dicts(str1_dict, str2_dict):
            for key in str1_dict.keys():
                val = str1_dict[key]
                if key not in str2_dict or str2_dict[key] != val:
                    return False
            return True
    
        if len(s2) < len(s1):
            return False
        
        small_s = s1
        big_s = s2
        
        small_s_dict = dict()
        big_s_dict = dict()
        
        j = 0
        while j < len(small_s):
            if small_s[j] not in small_s_dict:
                small_s_dict[small_s[j]] = 0
            small_s_dict[small_s[j]] += 1
            j += 1
        
        j = 0
        while j < len(small_s):
            if big_s[j] not in big_s_dict:
                big_s_dict[big_s[j]] = 0
            big_s_dict[big_s[j]] += 1
            j += 1
        
        i = 0
        while j < len(big_s):
            if compare_char_dicts(small_s_dict, big_s_dict):
                return True

            if big_s_dict[big_s[i]] == 1:
                del(big_s_dict[big_s[i]])
            else:
                big_s_dict[big_s[i]] -= 1
            
            if big_s[j] not in big_s_dict:
                big_s_dict[big_s[j]] = 1
            else:
                big_s_dict[big_s[j]] += 1
            
            i += 1
            j += 1
        
        if compare_char_dicts(small_s_dict, big_s_dict):
            return True
        
        return False

            