class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        que = deque()
        que.append((sr,sc))
        original = image[sr][sc]
        m,n = len(image),len(image[0])
        if image[sr][sc] == color:
            return image
        
        image[sr][sc] = color
        while que:
            i,j = que.popleft()
            for i_off,j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                r,c = i+i_off,j+j_off
                if 0<=r<m and 0<=c<n and image[r][c] == original:
                    image[r][c] = color
                    que.append((r,c))
        return image

                    

            
        