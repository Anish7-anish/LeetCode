class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom up DP
        # Time Complexity O(n^2)
        # Space Complexity O(n)
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
        