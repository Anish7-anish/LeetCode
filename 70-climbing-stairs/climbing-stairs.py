class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # dp = [0]*(n+1)

        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-2]+dp[i-1]

        # print(dp)

        # return dp[n]

        # memo = {1:1, 2:2}

        # def f(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = f(n-2) + f(n-1)
        #         return memo[n]
        
        # return f(n)

        #Bottom up Constant Space

        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(3, n+1):
            prev, cur = cur, prev+cur

        return cur
        
