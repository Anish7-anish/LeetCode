class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        for key,val in freq.items():
            if val>n//2:
                return key
