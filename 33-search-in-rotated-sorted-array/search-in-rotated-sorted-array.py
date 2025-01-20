class Solution:    
    def search(self, nums: List[int], target: int) -> int:
        def binary(arr,target,l,r):
            while l<=r:
                mid = (l+r)//2
                if arr[mid]==target:
                    return mid
                elif arr[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        
        # if len(nums)==1 and nums[0]==target:
        #     return 0
        # elif len(nums)==1 and nums[0]!=target:
        #     return -1

        n = len(nums)
        l = 0
        r = n-1

        while l < r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        
        
        
        piv = l
        
        if target == nums[piv]:
            return piv

        if target > nums[piv] and target > nums[n-1]:
            return binary(nums, target, 0, (piv-1))
        else:
            return binary(nums, target, piv+1, n-1)
        
        

        