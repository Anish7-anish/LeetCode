class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # i = 0
        # j = 1

        # # 2 pointer approach
        # max_profit = 0

        # while j < n:
        #     if prices[i] > prices[j]:
        #         i=j
        #         j+=1
        #     else:
        #         max_profit = max(max_profit, prices[j]-prices[i])
        #         j+=1

        # return max_profit

        n = len(prices)
        minn = prices[0]
        max_profit = 0

        for i in range(1,n):
            profit = prices[i] - minn
            max_profit = max(max_profit, profit)
            minn = min(minn, prices[i])

        return max_profit
                
        
        
        