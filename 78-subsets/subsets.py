class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            # base case
            if i == n:
                res.append(sol[:])
                return
            
            # Dont pick 
            backtrack(i+1)

            # Pick
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            

        backtrack(0)
        return res
        