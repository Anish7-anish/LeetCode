class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])

        prev = nums[0]
        cur = max(nums[0],nums[1])

        for i in range(2, n):
            prev, cur = cur, max((nums[i]+prev), cur)
        
        return cur
        