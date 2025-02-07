class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1,2:2}
        
        def stairs(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = stairs(x-1)+stairs(x-2)
                return memo[x]

        return stairs(n)        