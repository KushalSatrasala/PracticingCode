class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = 1
        if num < 0:
            neg = -1
            num = num * -1
        
        if num == 0:
            return "0"
        
        res_str = ""
        
        while num:
            rem = num % 7
            num = int(num / 7)
            res_str += str(rem)
        
        if neg == -1:
            res_str += "-"
        
        return res_str[::-1]