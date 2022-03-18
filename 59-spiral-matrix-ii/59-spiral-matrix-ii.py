class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1
        matrix = [ [None for _ in range(n)] for _ in range(n) ]
        top = 0
        bottom = n - 1
        left = 0 
        right = n - 1

        while left <= right:    
            k = left
            while k < right:
                matrix[top][k] = count
                count += 1
                k += 1
            
            k = top
            while k < bottom:
                matrix[k][right] = count
                count += 1
                k += 1
            
            k = right
            while k > left:
                matrix[bottom][k] = count
                count += 1
                k -= 1
            
            k = bottom
            while k > top:
                matrix[k][left] = count
                count += 1
                k -= 1
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        if count == n * n:
            matrix[n // 2][n // 2] = count
            
        
        return matrix
        
            
        
        