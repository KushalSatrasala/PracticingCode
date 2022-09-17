class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        odd = 0
        counter = collections.Counter(s)
        for ch in counter.keys():
            res += ( counter[ch] // 2 ) * 2
            if res % 2 == 0 and counter[ch] % 2 == 1:
                res += 1
        return res