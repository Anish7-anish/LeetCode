class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        print(m,n)

        r_b=0
        r_e=len(matrix)-1
        c_b=0
        c_e=len(matrix[0])-1

        l=[]

        if len(matrix)==0:
            return []

        while(r_b<=r_e and c_b<=c_e):
            for i in range(c_b,c_e+1):
                l.append(matrix[r_b][i])
            r_b+=1
            print("hi")
            for i in range(r_b,r_e+1):
                l.append(matrix[i][c_e])
            c_e-=1
            print("hello")
            if(r_b<=r_e):
                for i in range(c_e,c_b-1,-1):
                    l.append(matrix[r_e][i])
                r_e-=1
            if (c_b<=c_e):
                for i in range(r_e,r_b-1,-1):
                    l.append(matrix[i][c_b])
                c_b+=1
        return l
            
        

        