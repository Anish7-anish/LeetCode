class Solution:
    def countBits(self, n: int) -> List[int]:

        def one(n):
            ans = 0
            while n!=0:
                ans+=1
                n=n&(n-1)
            return ans

        res = []

        for i in range(n+1):
            res.append(one(i))

        return res
        