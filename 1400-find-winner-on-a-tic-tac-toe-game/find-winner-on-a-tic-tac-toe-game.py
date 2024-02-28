import numpy as np
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        winner= None
        mat=[[0 for _ in range(3)] for _ in range(3)]
        for i in range(len(moves)):
            if i%2==0:
                mat[(moves[i][0])][(moves[i][1])] = 2
            else:
                mat[(moves[i][0])][(moves[i][1])] = 5


        def checkWin(s):
            nonlocal winner
            if winner: return
            if s == 6:
                winner="A"
                
            if s== 15:
                winner="B"
                
        
        def checkRows():
            for row in mat:
                checkWin(sum(row))
        def checkCols():
            for col in zip(*mat):
                checkWin(sum(col))

        def checkDiagonal1():
            checkWin(mat[0][0] + mat[1][1] + mat[2][2])
        def checkDiagonal2():
            checkWin(mat[0][2] + mat[1][1] + mat[2][0])
        
        checkRows()
        checkCols()
        checkDiagonal1()
        checkDiagonal2()

        return winner or ('Draw' if len(moves) == 9 else 'Pending')
        
                

        