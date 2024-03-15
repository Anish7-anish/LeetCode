import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=0
        if n==0:
            return 1
        elif n==1:
            return x
        elif n>1:
            return x**n
        elif n<0:
            return (x**(n))
            

        
                


        