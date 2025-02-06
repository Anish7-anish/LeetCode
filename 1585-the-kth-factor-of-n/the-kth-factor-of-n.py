class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact_arr = []
        
        for j in range(1,n//2+1):
            if n%j==0:
                fact_arr.append(j)
                if len(fact_arr) == k:
                    return j
        fact_arr.append(n)
        if len(fact_arr) == k:
            return n

        if k > len(fact_arr):
            return -1

            
        

        