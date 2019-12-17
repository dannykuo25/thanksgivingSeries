# bfs solution
import collections
class Solution:
    def orangesRotting(self, grid):
        res = 0
        n, m = len(grid), len(grid[0])
        cnt = 0
        Q = collections.deque([])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: cnt += 1
                if grid[i][j] == 2: Q.append([i, j])
        
        while Q: #
            for _ in range(len(Q)):
                i, j = Q.popleft() # [2, 2]
                for x, y in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        Q.append([x, y]) # 
                        cnt -= 1 # 0
            res += 1 # 5
        return max(0, res-1) if cnt == 0 else -1
# grid = [[2,1,1],[1,1,0],[0,1,1]]
# 2 2 2
# 2 2 0
# 0 2 2




class Solution2:
    def orangesRotting(self, grid):
        if not grid:
            return -1
        # only zero
        if self.noOneTwo(grid):
            return 0
        # iso or only fresh without rotting oranges
        if self.impossible(grid):
            return -1
        step = 0
        while self.contain(grid):            
            posList = self.rottingPos(grid)
            for i in range(len(posList)):
                self.turn(grid, posList[i])
            step += 1
        return step

    def noOneTwo(self, grid):
        noOne, noTwo = True, True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    noOne = False
                if grid[i][j] == 2:
                    noTwo = False
        return noOne and noTwo
    # one of the fresh oranges is isolated
    def impossible(self, grid):
        noTwo = True
        iso = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isolate(grid, i, j):
                    iso = True
                if grid[i][j] == 2:
                    noTwo = False
        return noTwo or iso
    
    def isolate(self, grid, i, j):
        if grid[i][j] == 1:
            if (i-1 < 0 or grid[i-1][j] == 0) and (i+1 >= len(grid) or grid[i+1][j] == 0) and (j-1 < 0 or grid[i][j-1] == 0) and (j+1 >= len(grid[0]) or grid[i][j+1] == 0):
                return True
        return False

    # contain 1 and 2 in the grid
    def contain(self, grid):
        one, two = False, False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    one = True
                if grid[i][j] == 2:
                    two = True    
                if one and two:
                    return True
        return one and two

    # record this round rotting position
    def rottingPos(self, grid):
        
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    res.append([i, j])
        print(res)
        return res
    # turn neighbor freshing oranges to rotting oranges
    def turn(self, grid, pos):
        i, j = pos[0], pos[1]
        if i-1 >= 0 and grid[i-1][j] == 1:
            grid[i-1][j] = 2
        if i+1 < len(grid) and grid[i+1][j] == 1:
            grid[i+1][j] = 2
        if j-1 >= 0 and grid[i][j-1] == 1:
            grid[i][j-1] = 2
        if j+1 < len(grid[0]) and grid[i][j+1] == 1:
            grid[i][j+1] = 2



    # # at least one rotting orange's(2) neighbor is fresh orange(1)            
    # def canMove(self, grid):
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 2:
    #                 if (i-1 > 0 and grid[i-1][j] == 1) or (i+1 < len(grid) and grid[i+1][j] == 1) or (j-1 > 0 and grid[i][j-1] == 1) or (j+1 < len(grid[0]) and grid[i][j+1] == 1):
    #                     return True
    #     return False
    # # turn every fresh oranges near rotting orange to rotting    1 -> 2
    # def move(self, grid):
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 2:
    #                 if i-1 >= 0 and grid[i-1][j] == 1:
    #                     grid[i-1][j] = 2
    #                 if i+1 < len(grid) and grid[i+1][j] == 1:
    #                     grid[i+1][j] = 2
    #                 if j-1 >= 0 and grid[i][j-1] == 1:
    #                     grid[i][j-1] = 2
    #                 if j+1 < len(grid[0]) and grid[i][j+1] == 1:
    #                     grid[i][j+1] = 2


# grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[1],[1],[1],[1]]
ans = Solution().orangesRotting(grid)
print(ans)