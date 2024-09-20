class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 1
        suff = 1
        ans = - float('inf')

        for i in range(len(nums)):
            if pref == 0: pref =1
            if suff == 0: suff =1

            pref *= nums[i]
            suff *= nums[-i-1]

            ans = max(ans, max(pref,suff))
        return ans
        