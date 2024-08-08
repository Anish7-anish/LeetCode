class Solution:
    def search(self, nums):
        target=0
        start=0
        end=len(nums)-1
        

        while(start<=end):
            mid=(start+end)//2

            if nums[mid] == target:
                return len(nums[:mid])
            elif target>nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return len(nums[:start])

    def countNegatives(self, grid: List[List[int]]) -> int:
        nums=[-1,0,2,3,4]
        sum=0
        for i in grid:
            i = [x for j, x in enumerate(i) if not (x == 0 and j > i.index(0))]
            a=self.search(sorted(i))
            sum+=a
            print(a)
        return sum
        
        