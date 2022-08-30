class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ""
        slen = len(s)
        cur_val = 0
        i = slen - 1
        while i >= 0:
            cur_val += shifts[i]
            cur = ord(s[i]) - 97
            nxt = (cur + cur_val) % 26
            res += chr(nxt + 97)
            i -= 1
        return res[::-1]