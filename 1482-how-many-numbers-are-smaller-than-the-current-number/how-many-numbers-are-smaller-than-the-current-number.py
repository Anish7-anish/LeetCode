class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = defaultdict(int)
        nums2 = nums[:]
        nums2.sort()

        for i,val in enumerate(nums2):
            if val not in ans: 
                ans[val] = i
        print(ans)
        
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = ans[nums[i]]
        return res
        
        
        
        