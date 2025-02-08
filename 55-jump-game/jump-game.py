class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0]*n
        dp[n-1] = 1
        cur_end = n-1

        for i in range(n-2,-1,-1):
            if cur_end - i <= nums[i]:
                dp[i] = 1
                cur_end = i
        print(dp)
            
        return True if dp[0] == 1 else False

        