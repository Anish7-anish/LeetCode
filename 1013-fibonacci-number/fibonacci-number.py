class Solution:
    def fib(self, n: int) -> int:
        # Naive Recursive Solution

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        
        # return self.fib(n-1)+self.fib(n-2)

        # Top Down DP Memoization
        
        # memo = {0:0,1:1}

        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x] = f(x-1)+f(x-2)
        #         return memo[x]
        
        # return f(n)

        # Bottom Up Tabulation approach

        if n < 2:
            return n
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
        



        