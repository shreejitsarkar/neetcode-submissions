class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice=prices[0]
        for i in prices:
            
            minprice=min(minprice,i)
            
            profit=i-minprice
            maxprofit=max(maxprofit,profit)
        return maxprofit

