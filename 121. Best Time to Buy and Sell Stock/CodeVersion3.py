class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i,j = 0,1
        maxPrice = float("-inf")

        while j<len(prices):
            maxPrice = max(maxPrice, prices[j]-prices[i])
            if prices[j] < prices[i]:
                i = j
            j += 1
        return 0 if maxPrice < 0 else maxPrice
        
