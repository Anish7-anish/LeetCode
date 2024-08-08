class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=0
        end=len(nums)-1

        l=-1
        r=-1
    
        while(start<=end):
            mid=(start+end)//2
            if nums[mid] == target:
                l=mid
                r=mid

                while(l>0 and nums[l-1] == target):
                    l=l-1
                while(r<len(nums)-1 and nums[r+1] == target):
                    r=r+1
                break
            elif target>nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return [l,r]

    

        


        