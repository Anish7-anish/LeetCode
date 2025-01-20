class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        longest = 0

        n = len(nums)
        for r in range(n):
            # print('r',r)
            if nums[r] == 0:
                k-=1
            
            if k>=0:
                w = (r-l)+1
                longest = max(w,longest)
                # print('longest',longest)
            else:
                while k < 0:
                    l+=1
                    if nums[l-1] == 0:
                        k+=1
        return longest
        