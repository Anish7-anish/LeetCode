class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = float('inf')
        cur_sum = 0
        n = len(nums)
        for r in range(n):
            if cur_sum<target:
                cur_sum+=nums[r]
            
            while cur_sum>=target:
                w = (r-l)+1
                min_len = min(w,min_len)
                cur_sum-=nums[l]
                l+=1
        return min_len if min_len!=float('inf') else 0
                

        