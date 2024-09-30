class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        maxarea = 0

        left = 0
        right = n - 1

        while left < right:
            h = min(height[left], height[right]) 
            width =  right - left
            area = h * width
            maxarea = max(maxarea, area)

            if height[left] > height[right]:
                right-=1
            else:
                left+=1

        return maxarea     