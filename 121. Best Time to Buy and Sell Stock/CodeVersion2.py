class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Looping through the array using two Ponters:- Pointer1 will detect day of buying - Another Pointer2 will detect the best day to sell. 

        Pointer1, Pointer2 = 0,1
        max = 0
        while Pointer2 < len(prices):
            if prices[Pointer2] - prices[Pointer1] < 0:
                Pointer1 = Pointer2
                Pointer2 += 1
            else:
                if max < prices[Pointer2] - prices[Pointer1]:
                    max = prices[Pointer2] - prices[Pointer1]
                Pointer2 += 1
        return max