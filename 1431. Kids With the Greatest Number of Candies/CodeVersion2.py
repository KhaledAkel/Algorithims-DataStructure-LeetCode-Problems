class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        return [x + extraCandies >= maxVal for x in candies]
