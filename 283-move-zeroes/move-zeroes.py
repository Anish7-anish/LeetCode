class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=nums.count(0)
        for i in range(0,c):
            nums.remove(0)
        print(nums)
        for i in range(0,c):
            nums.append(0)
        print(nums)
        