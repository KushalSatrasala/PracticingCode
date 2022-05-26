class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        
        i = 0
        while i < m:
            j = 0
            while j < n:
                if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]:
                    return False
                rows[i].add(matrix[i][j])
                cols[j].add(matrix[i][j])
                
                j += 1
            i += 1
        
        return True