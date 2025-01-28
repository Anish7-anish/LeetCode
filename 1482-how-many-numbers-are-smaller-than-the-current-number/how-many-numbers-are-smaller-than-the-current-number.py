class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = defaultdict(int)
        nums2 = nums[:]
        nums2.sort()

        for i in range(len(nums2)):
            if i == 0:
                ans[nums2[i]]==0
            if nums2[i]==nums2[i-1]:
                ans[nums2[i]]=ans[nums2[i-1]]
            else:
                ans[nums2[i]]=i
        
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = ans[nums[i]]
        return res
        
        
        
        