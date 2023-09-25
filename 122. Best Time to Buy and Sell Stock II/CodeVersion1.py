class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Pointer1, Pointer2 = 0,1
        max = 0
        while Pointer2 < len(prices):
            if prices[Pointer2] - prices[Pointer1] < 0:
                Pointer1 = Pointer2
                Pointer2 += 1
            else:
                max += prices[Pointer2] - prices[Pointer1]
                
                Pointer1 += 1
                Pointer2 += 1
        return max
