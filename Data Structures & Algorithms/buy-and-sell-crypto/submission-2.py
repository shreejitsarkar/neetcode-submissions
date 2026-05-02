class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<minvalue:
                minvalue=prices[i]
            currprofit=prices[i]-minvalue
            profit=max(profit,currprofit)
        return profit

        