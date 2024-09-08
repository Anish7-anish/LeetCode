class Solution:
    def binsearch(self,nums,target,l,r):
        n=len(nums)

        while l <= r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1

        while l < r:
            mid=(l+r)//2
            
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        print(l,r)
        if nums[l]<=target and nums[n-1]>=target:
            return self.binsearch(nums,target,l,n-1)
        else:
            return self.binsearch(nums,target,0,r-1)

        