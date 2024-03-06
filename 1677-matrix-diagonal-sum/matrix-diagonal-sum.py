class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        dsum=0
        
            
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    dsum+=mat[i][j]

        for i in range(len(mat)):
            for j in range(len(mat)):
                if i+j==len(mat)-1:
                    dsum+=mat[i][j]
        if len(mat)%2==0:
            return dsum
        else:
            return dsum - mat[len(mat)//2][len(mat)//2]
        