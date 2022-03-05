class Solution:
    def reverseWords(self, s: str) -> str:
        str_split = s.split()
        res = []
        for i in str_split:
            res.append(i[::-1])
        return " ".join(res)