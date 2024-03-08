class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = [row[:] for row in matrix]
        
        
        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix_copy[i][j] == 0:
                    matrix[i][:] = [0]*len(matrix[0])
                    new_column_values = [0] * len(matrix)
                    for k in range(len(matrix)):
                        matrix[k][j] = new_column_values[k]

                    

                    
                    
        

        