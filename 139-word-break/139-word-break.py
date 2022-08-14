class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        slen = len(s)
        dp = dict()
        
        def breakdown(s, slen, start):
            if start >= slen:
                return True
            if start in dp:
                return dp[start]
            if s in words:
                dp[start] = True
                return True
            
            i = start
            while i <= slen:
                while i < slen and s[start:i] not in words:
                    i += 1
                if i == slen and s[start:] not in words:
                    dp[start] = False
                    return False
                ret_val = breakdown(s, slen, i)
                if ret_val:
                    dp[start] = True
                    return True
                i += 1
            return False
        
        return breakdown(s, slen, 0)