class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If list consist of one day we just return 0 becuase you can not buy and sell at the same day. 
        if len(prices) <2:
            return 0

        # Looping through the array using two Ponters:- Pointer1 will detect day of buying - Another Pointer2 will detect the best day to sell. 
        Pointer1, Pointer2 = 0,1

        max = prices[Pointer2] - prices[Pointer1]
        while Pointer2 <= len(prices)-1:
            if prices[Pointer2] - prices[Pointer1] < 0:
                Pointer1 = Pointer2
                Pointer2 += 1
            else:
                if max < prices[Pointer2] - prices[Pointer1]:
                    max = prices[Pointer2] - prices[Pointer1]
                Pointer2 += 1
        if max < 0:
            return 0
        else:
            return max