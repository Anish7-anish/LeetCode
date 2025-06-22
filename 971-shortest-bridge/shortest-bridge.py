class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f_x, f_y = -1, -1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    f_x, f_y = i,j
                    break

        def dfs(i,j):
            grid[i][j] = 2
            bfs_queue.append((i,j))
            for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                r,c = i+i_off, j+j_off
                if 0<=r<n and 0<=c<n and grid[r][c] == 1:
                    dfs(r,c)
        
        bfs_queue = deque()
        dfs(f_x,f_y)

        distance = 0
        while bfs_queue:
            new_bfs = deque()
            size = len(bfs_queue)
            for i in range(size):
                x,y = bfs_queue.popleft()
                for x_off, y_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                    cur_x, cur_y = x+x_off, y+y_off
                    if 0<=cur_x<n and 0<=cur_y<n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs.append((cur_x,cur_y))
                            grid[cur_x][cur_y] = -1
            
            bfs_queue = new_bfs
            distance+=1
        
        return distance



        