class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        leadingZero = True
        digit = 1
        res = 0

        for ele in s:
            if ele == " ":
                if not leadingZero:
                    break
                else:
                    continue

            if ele == "-" or ele == "+":
                if not leadingZero:
                    break
                neg = ele == "-"
                leadingZero = False
                continue

            if ele.isdigit():
                leadingZero = False
                if not leadingZero:
                    res = res * 10 + int(ele)
                    digit *= 10
            else:
                break

        return min(max(-res if neg else res, -2 ** 31), 2 ** 31 - 1)
