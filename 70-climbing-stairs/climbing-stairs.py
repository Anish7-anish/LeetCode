class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {1:1,2:2}
        
        # def stairs(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x] = stairs(x-1)+stairs(x-2)
        #         return memo[x]

        # return stairs(n)

        # Top down

        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(3,n+1):
            prev,cur = cur, prev+cur
        return cur  