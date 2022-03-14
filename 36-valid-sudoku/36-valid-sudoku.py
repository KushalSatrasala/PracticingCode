class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = [ set() for i in range(9) ]
        rows = [ set() for i in range(9) ]
        sqs = [ set() for i in range(9) ]
        
        i = 0
        add = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] == ".":
                    pass
                else:
                    if board[i][j] in sqs[ add + int(j / 3) ]:
                        return False
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in cols[j]:
                        return False
                    sqs[ add + int(j / 3) ].add(board[i][j])
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                j += 1
            i += 1
            if i % 3 == 0:
                add += 3
            
        
        return True