class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        num_islands = 0

        def dfs(i,j):
            for i_off,j_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                r,c = i+i_off,j+j_off
                if 0<=r<m and 0<=c<n and grid[r][c] == "1":
                    grid[r][c] = "0"
                    dfs(r,c)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands+=1
                    dfs(i,j)
        
        return num_islands