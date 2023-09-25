class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        total = n
        while total != 1:
            if total in seen:
                return False
            seen.add(total)
            total = sum(int(num) ** 2 for num in str(total))
        return True
