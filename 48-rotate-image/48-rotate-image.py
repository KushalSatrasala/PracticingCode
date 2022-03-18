class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        
        while left < right:
            
            k = 0
            while k < (right - left):
                temp = matrix[top][left + k]
                matrix[top][left + k] = matrix[bottom - k][left]
                matrix[bottom - k][left] = matrix[bottom][right - k]
                matrix[bottom][right - k] = matrix[top + k][right]
                matrix[top + k][right] = temp
                k += 1
            
            print(matrix)
            
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            
            print(left, right, top, bottom)