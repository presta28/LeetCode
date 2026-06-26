class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        min_price=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                profit = prices[i]-min_price+profit
                min_price=prices[i]
        return profit
        