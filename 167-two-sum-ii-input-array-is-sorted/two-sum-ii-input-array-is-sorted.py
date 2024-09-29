class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        i = 0
        j = len(nums)-1

        while i < j:
            cur_sum = nums[i] + nums[j]
            if target == cur_sum:
                return [i+1,j+1]
            elif target > cur_sum:
                i+=1
            else:
                j-=1

            
                