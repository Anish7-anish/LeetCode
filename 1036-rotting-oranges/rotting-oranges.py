class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        m,n = len(grid),len(grid[0])
        num_minutes = -1
        num_fresh = 0


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i,j))
                elif grid[i][j] == 1:
                    num_fresh+=1
        
        if num_fresh == 0:
            return 0
  
        while que:
            size = len(que)
            num_minutes += 1
            for _ in range(size):
                i,j = que.popleft()
                for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                    r,c = i+i_off,j+j_off
                    if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                            que.append((r,c))
                            grid[r][c] = 2
                            num_fresh-=1
                        
        return num_minutes if num_fresh == 0 else -1
        
        
        