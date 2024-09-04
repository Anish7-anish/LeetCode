class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0

        left=0
        right=len(height)-1

        while left<right:
            h=min(height[left],height[right])
            w=right-left
            area = h*w
            maxarea = max(maxarea,area)

            if height[left]<height[right]:
                left+=1
            elif height[left]>height[right]:
                right-=1
            else:
                left+=1
                right-=1
        return maxarea
        