class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        def dfs(i,j):
            if i < 0 or i >=m or j<0 or j>=n or grid[i][j]!=1:
                return
            else:
                length[0]+=1
                grid[i][j]=0
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        

        max_length = [0]
        length = [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    max_length[0] = max(max_length[0],length[0])
                    length[0]=0
        
        return max_length[0]
        