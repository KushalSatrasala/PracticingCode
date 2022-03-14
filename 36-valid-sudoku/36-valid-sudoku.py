class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [[0]*n for _ in range(n)]
        cols = [[0]*n for _ in range(n)]
        boxes = [[0]*n for _ in range(n)]
 
        
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                
                if val == '.':
                    continue
                pos = int(val)-1
                
                if rows[r][pos]==1:
                    return False
                rows[r][pos] = 1
                
                if cols[c][pos]==1:
                    return False
                cols[c][pos] = 1
                
                box = (r//3)*3 + c//3
                if boxes[box][pos]:
                    return False
                boxes[box][pos] = 1
                
        return True