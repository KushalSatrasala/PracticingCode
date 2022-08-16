class Solution:
    def numDecodings(self, s: str) -> int:
        slen = len(s)
        dp = [None for _ in range(slen + 1)]
        dp[slen] = 1

        if s[0] == "0":
            return 0

        i = slen - 1
        while i >= 0:
            if s[i] == "0":
                i -= 1
                continue
            else:
                add_val = 0
                if (s[i] == "1" or s[i] == "2") and i + 1 < slen and s[i + 1] == "0":
                    if dp[i + 2] == None:
                        return 0
                    add_val = dp[i + 2]
                elif (s[i] != "1" or s[i] != "2") and i + 1 < slen and s[i + 1] == "0":
                    return 0
                else:
                    add_val = dp[i + 1]
                    if i + 1 < slen:
                        tmp = int(s[i] + s[i + 1])
                        if tmp <= 26 and dp[i + 2] != None:
                            add_val += dp[i + 2]
                dp[i] = add_val
                i -= 1
        return dp[0]