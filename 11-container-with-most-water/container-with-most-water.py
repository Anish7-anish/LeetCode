class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxarea=0
        lo=0
        hi=n-1

        while lo < hi:
            width = (hi-lo)
            length = min(height[lo],height[hi])
            area = (width*length)
            maxarea = max(maxarea,area)

            if height[lo]>height[hi]:
                hi-=1
            else:
                lo+=1
        
        return maxarea
