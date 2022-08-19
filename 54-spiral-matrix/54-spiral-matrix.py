class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n - 1
        top = 0 
        bottom = m - 1
        res = list()
        
        while left < right and top < bottom:
            i = 0
            while left + i <= right:
                res.append(matrix[top][left + i])
                i += 1
            top += 1
            
            i = 0
            while top + i <= bottom:
                res.append(matrix[top + i][right])
                i += 1
            
            i = 0
            right -= 1
            while right - i >= left:
                res.append(matrix[bottom][right - i])
                i += 1
            
            i = 0
            bottom -= 1
            while bottom - i >= top:
                res.append(matrix[bottom - i][left])
                i += 1
            left += 1
        
        if top == bottom and left <= right:
            i = 0 
            while left + i <= right:
                res.append(matrix[top][left + i])
                i += 1
        elif left == right and top <= bottom:
            i = 0 
            while top + i <= bottom:
                res.append(matrix[top + i][left])
                i += 1
            
        
        return res
            
                