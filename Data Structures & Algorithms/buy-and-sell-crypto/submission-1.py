class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                try: 
                    sell = prices[i+1]
                    buy = prices[i]
                except: 
                    pass
            elif prices[i] > sell:
                sell = prices[i]
            profit = max(profit, sell-buy)
        return profit
        
