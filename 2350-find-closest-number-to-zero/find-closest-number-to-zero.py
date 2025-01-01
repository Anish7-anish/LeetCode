class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')
        for i in nums:
            if abs(i) < abs(closest):
                closest = i
            elif abs(i) == abs(closest):
                closest = i if i > closest else closest

        return closest
        