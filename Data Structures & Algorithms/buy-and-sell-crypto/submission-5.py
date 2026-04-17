class Solution:
    def maxProfit(self, prices: List[int]) -> int:
 
        profit = 0

        l = 0

        window = ()

        for r in range(len(prices)):
            
            cur_profit = prices[r] - prices[l]

            if cur_profit < 0:
                l = r

            profit = max(cur_profit, profit) 
            
        return profit
            