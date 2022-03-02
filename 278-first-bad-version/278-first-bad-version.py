# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 0 
        high = n
        bad_found = False
        
        while low <= high:
            mid = int((low + high) / 2)
            if isBadVersion(mid):
                bad_found = True
                if mid - 1 >= 0 and not isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid - 1  
            else:
                low = mid + 1
        
        if not bad_found:
            return -1
        else:
            return mid
                