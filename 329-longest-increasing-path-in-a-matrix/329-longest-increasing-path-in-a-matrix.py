class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def tranverseMatrix(matrix, i, j, m, n, dp_map):
            if (i, j) in dp_map:
                return dp_map[(i, j)]
            
            max_val = 0
            if i - 1 >= 0 and matrix[i - 1][j] >  matrix[i][j]:
                ret_val = tranverseMatrix(matrix, i - 1, j, m, n, dp_map)
                if not max_val or ret_val > max_val:
                    max_val = ret_val
            
            if j - 1 >= 0 and matrix[i][j - 1] >  matrix[i][j]:
                ret_val = tranverseMatrix(matrix, i, j - 1, m, n, dp_map)
                if not max_val or ret_val > max_val:
                    max_val = ret_val
            
            if i + 1 < m and matrix[i + 1][j] >  matrix[i][j]:
                ret_val = tranverseMatrix(matrix, i + 1, j, m, n, dp_map)
                if not max_val or ret_val > max_val:
                    max_val = ret_val
            
            if j + 1 < n and matrix[i][j + 1] >  matrix[i][j]:
                ret_val = tranverseMatrix(matrix, i, j + 1, m, n, dp_map)
                if not max_val or ret_val > max_val:
                    max_val = ret_val
            
            dp_map[(i, j)] = max_val + 1
            return max_val + 1
            
        
        m = len(matrix)
        n = len(matrix[0])
        dp_map = dict()
        
        i = 0
        while i < m:
            j = 0
            while j < n:
                if (i, j) not in dp_map:
                    ret_val = tranverseMatrix(matrix, i, j, m, n, dp_map)
                    dp_map[(i, j)] = ret_val
                j += 1
            i += 1
        
        return max(list(dp_map.values()))