class Solution:
    def numIslands(self, grid):
        # corner case
        if not grid:
            return 0
        if len(grid) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        # another way to create a 2d array
        # visited = [[0]*n for i in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, visited, i, j)
        return cnt
    
    def dfs(self, grid, visited, i, j):
        
        visited[i][j] = 1
        
        if j + 1 < len(grid[0]) and grid[i][j + 1] == '1' and visited[i][j + 1] == 0:
            self.dfs(grid, visited, i, j + 1)
            
        if j - 1 >= 0 and grid[i][j - 1] == '1' and visited[i][j - 1] == 0:
            self.dfs(grid, visited, i, j - 1)
            
        if i + 1 < len(grid) and grid[i + 1][j] == '1' and visited[i + 1][j] == 0:
            self.dfs(grid, visited, i + 1, j)
            
        if i - 1 >= 0 and grid[i - 1][j] == '1' and visited[i - 1][j] == 0:
            self.dfs(grid, visited, i - 1, j)
        
grid = [["0","1","0"],["1","0","1"],["0","1","0"]]

print(Solution().numIslands(grid))