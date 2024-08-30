class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_value=min(prices)
        # min_index = prices.index(min_value)

        # if min_index==len(prices)-1:
        #     return 0
        # else:
        #     max_value = max(prices[min_index+1:])
        #     return max_value-min_value

        i,j=0,1
        max_profit=0

        while j<len(prices):
            if prices[i]<=prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
                j+=1
            elif prices[i]>prices[j]:
                i=j
                j+=1
        return max_profit
                
        
        
        