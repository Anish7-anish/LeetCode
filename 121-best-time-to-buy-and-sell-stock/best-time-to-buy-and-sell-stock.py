class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = float('-inf')
        i,j = 0,1

        while j<len(prices):
            if prices[i]>prices[j]:
                i=j
                j+=1
            else:
                prof = prices[j]-prices[i]
                max_prof = max(prof, max_prof)
                j+=1
        
        if max_prof < 0:
            return 0
        else:
            return max_prof