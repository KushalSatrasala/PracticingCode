class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp_arr = list()
        dp_arr.append(0)
        dp_arr.append(1)
        
        if n == 0:
            return 0
    
        max_val = 1
        if n <= 2:
            return 1
        
        i = 2
        while i <= n:
            if i % 2 == 0:
                val = dp_arr[ int(i / 2) ]
            else:
                val = dp_arr[ int(i / 2) ] + dp_arr[ int(i / 2) + 1]
            
            if val > max_val:
                max_val = val
            
            dp_arr.append(val)
            
            i += 1
        
        return max_val