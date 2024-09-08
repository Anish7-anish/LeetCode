class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        t=row*col
        left=0
        right=t-1


        while left<=right:
            mid = (left+right)//2

            i = mid // col
            j = mid % col

            mid_num = matrix[i][j]

            if mid_num == target:
                return True
            elif target < mid_num:
                right = mid-1
            else:
                left = mid+1
        return False