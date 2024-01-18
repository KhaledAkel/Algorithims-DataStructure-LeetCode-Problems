class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a, b = 1, max(piles)
        k = b

        while a < b:
            mid = (a + b) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours > h:
                a = mid + 1
            else:
                k = min(mid, k)
                b = mid

        return k
