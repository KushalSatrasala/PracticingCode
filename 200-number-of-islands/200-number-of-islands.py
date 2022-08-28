class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = collections.deque()
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        i = 0
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] == "1":
                    islands += 1
                    queue.append((i, j))
                    while queue:
                        r, c = queue.popleft()
                        if grid[r][c] == "0":
                            continue
                        grid[r][c] = "0"
                        if r + 1 < m and grid[r + 1][c] == "1":
                            queue.append((r + 1, c))
                        if r - 1 >= 0 and grid[r - 1][c] == "1":
                            queue.append((r - 1, c))
                        if c + 1 < n and grid[r][c + 1] == "1":
                            queue.append((r, c + 1))
                        if c - 1 >= 0 and grid[r][c - 1] == "1":
                            queue.append((r, c - 1))
                j += 1
            i += 1
        
        return islands
                            
        