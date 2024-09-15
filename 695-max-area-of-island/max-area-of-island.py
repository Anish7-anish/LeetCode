class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        length = [0]
        def dfs(i,j):
            
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            else:
                grid[i][j] = 0
                length[0]+=1
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)

            return length[0]



        maxlength = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    a = dfs(i,j)
                    maxlength = max(maxlength, a)
                    length[0] = 0

        return maxlength

        