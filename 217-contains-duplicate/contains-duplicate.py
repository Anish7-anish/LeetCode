class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        sett = set()

        for i in nums:
            if i not in sett:
                sett.add(i)
            else:
                return True

        return False
        