class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        counter = {}
        for i in nums:
            if i in counter:
                counter[i]+= 1
            else:
                counter[i] = 1
        for i in counter:
            if counter[i] > (n // 2):
                return i
            
        