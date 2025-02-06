class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        summ = 0

        
        for i in range(n):
            summ+=mat[i][i]
            summ+=mat[i][n-i-1]
        
        if n%2!=0:
            summ = summ-mat[n//2][n//2]
        
        return summ
        
            


        