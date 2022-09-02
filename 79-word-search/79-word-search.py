class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dp_map = dict()
        m = len(board)
        n = len(board[0])
        def travel_thru(row, col, board, word, i):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[i]:
                return False
            
            if i == len(word) - 1:
                return True
            
            cur_word = board[row][col]
            board[row][col] = "#"

            flag = travel_thru(row + 1, col, board, word, i + 1)
            if flag:
                board[row][col] = cur_word
                return True
            
            flag = travel_thru(row - 1, col, board, word, i + 1)
            if flag:
                board[row][col] = cur_word
                return True
            
            flag = travel_thru(row, col + 1, board, word, i + 1)
            if flag:
                board[row][col] = cur_word
                return True
            
            flag = travel_thru(row, col - 1, board, word, i + 1)
            if flag:
                board[row][col] = cur_word
                return True
            
            board[row][col] = cur_word
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag = travel_thru(i, j, board, word, 0)
                    if flag:
                        return True
        return False