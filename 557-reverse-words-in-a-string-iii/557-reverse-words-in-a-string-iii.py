class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res_str = ""
        for word in words:
            right = len(word) - 1
            while right >= 0:
                res_str += word[right]
                right -= 1
            res_str += " "
        return res_str[:-1]