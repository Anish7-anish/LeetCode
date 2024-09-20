class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        sett = set()

        for i in nums:
            print(i)
            if i in sett:
                return True
            else:
                sett.add(i)

        return False
        