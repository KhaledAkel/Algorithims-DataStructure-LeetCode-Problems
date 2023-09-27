class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        MAX = max(candies)
        results = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= MAX:
                results[i] = True

        return results

