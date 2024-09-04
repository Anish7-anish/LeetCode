class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        n=len(nums)
        nums.sort()

        for i in range(0,len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            lo,hi=i+1,n-1

            while(lo<hi):
                summ = nums[i]+nums[lo]+nums[hi]

                if summ == 0:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    lo+=1
                    hi-=1
                    while lo<hi and nums[lo]==nums[lo-1]:
                        lo+=1
                    while lo<hi and nums[hi]==nums[hi+1]:
                        hi-=1
                elif summ > 0:
                    hi-=1
                else:
                    lo+=1
        return ans


        
        