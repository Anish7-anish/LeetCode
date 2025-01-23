class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -nums[i]
        print(nums)
        
        heapq.heapify(nums)
        
        i = 1
        while i <= k:
            x = -heapq.heappop(nums)
            i=i+1
        return x



