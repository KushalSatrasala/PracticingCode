class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def paths(i, j, m, n, dp_map, obstacleGrid):
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                dp_map[(i, j)] = 0
                return 0
            if i == m - 1 and j == n - 1:
                if obstacleGrid[i][j] == 1:
                    dp_map[(i, j)] = 0
                    return 0
                else:
                    dp_map[(i, j)] = 1
                    return 1
            
            if (i, j) in dp_map:
                return dp_map[(i, j)]
            bottom = paths(i + 1, j, m, n, dp_map, obstacleGrid)
            right = paths(i, j + 1, m, n, dp_map, obstacleGrid)
            dp_map[(i, j)] = bottom + right
            return dp_map[(i, j)]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp_map = dict()
        paths(0, 0, m, n, dp_map, obstacleGrid)
        return dp_map[(0, 0)]