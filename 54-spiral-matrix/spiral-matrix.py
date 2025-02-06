class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m , n = len(matrix), len(matrix[0])
        UP = 1
        DOWN = 2
        RIGHT = 3
        LEFT = 4
        DIRECTION = RIGHT

        UP_WALL = 0
        DOWN_WALL = m
        LEFT_WALL = -1
        RIGHT_WALL = n

        ans = []
        i,j = 0,0

        while len(ans)<(m*n):
            if DIRECTION == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j+=1
                DIRECTION = DOWN
                i+=1
                j-=1
                RIGHT_WALL -=1
            elif DIRECTION == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i+=1
                DIRECTION = LEFT
                i-=1
                j-=1
                DOWN_WALL-=1
            elif DIRECTION == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j-=1
                DIRECTION = UP
                i-=1
                j+=1
                LEFT_WALL+=1
            elif DIRECTION == UP:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i-=1
                DIRECTION = RIGHT
                i+=1
                j+=1
                UP_WALL+=1
        
        return ans


            
            
        