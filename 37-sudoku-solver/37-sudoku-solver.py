class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(10)]
        cols = [set() for _ in range(10)]
        
        dp_map = dict()
        dp_map[(0,0)] = set()
        dp_map[(0,1)] = set()
        dp_map[(0,2)] = set()
        dp_map[(1,0)] = set()
        dp_map[(1,1)] = set()
        dp_map[(1,2)] = set()
        dp_map[(2,0)] = set()
        dp_map[(2,1)] = set()
        dp_map[(2,2)] = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    dp_map[(i // 3, j // 3)].add(board[i][j])

        def tranverse_board():
            found = False
            row, col = None, None
            
            #Find next dot cell
            for i in range(0, 9):
                for j in range(0, 9):
                    if board[i][j] == ".":
                        row, col = i,j
                        found = True
                        break
                if found:
                    break
            
            if found == False:
                return True
            
            for k in range(1, 10):
                k_str = str(k)
                if k_str not in rows[row] and k_str not in cols[col] and k_str not in dp_map[(row // 3, col // 3)]:
                    board[row][col] = k_str
                    rows[row].add(k_str)
                    cols[col].add(k_str)
                    dp_map[(row // 3, col // 3)].add(k_str)
                    flag = tranverse_board()
                    if flag:
                        return True
                    rows[row].remove(k_str)
                    cols[col].remove(k_str)
                    dp_map[(row // 3, col // 3)].remove(k_str)
            
            board[row][col] = "."
            return False
        
        tranverse_board()