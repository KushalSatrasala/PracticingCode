class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = ""

        if x < 0:
            return False
        if x < 10:
            return True

        while x:
            str1 += str(x % 10)
            x = int(x / 10)

        i = 0 
        j = len(str1) - 1
        
        while i < j:
            if str1[i] != str1[j]:
                return False
            i += 1
            j -= 1
        
        return True
            
        
            