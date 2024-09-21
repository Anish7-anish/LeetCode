class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin(nums,target,left,right):
            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        if len(nums)==1 and nums[0]==target:
            return 0
        elif len(nums)==1 and nums[0]!=target:
            return -1

        n = len(nums)
        l=0
        r = n-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        
        piv = l
        print(piv)
        
        if target == nums[piv]:
            return piv

        if target > nums[piv] and target > nums[n-1]:
            return bin(nums, target, 0, (piv-1))
        else:
            return bin(nums, target, piv+1, n-1)
        