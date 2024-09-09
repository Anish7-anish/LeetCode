class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        min_length = float('inf')
        n = len(nums)
        cur_sum = 0

        for r in range(n):
            cur_sum += nums[r]

            while cur_sum >= target:
                min_length = min(min_length, (r-l)+1)
                cur_sum -= nums[l]        
                l+=1
            
            
        if min_length == float('inf'):
            return 0
        return min_length