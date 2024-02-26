class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c=0
        d=0
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                c+=1
            else:
                break
        if c==len(nums)-1:
            return True

        for i in range(0,len(nums)-1):
            if nums[i]>=nums[i+1]:
                d+=1
            else:
                break
        if d==len(nums)-1:
            return True
        return False

        
                
            

        