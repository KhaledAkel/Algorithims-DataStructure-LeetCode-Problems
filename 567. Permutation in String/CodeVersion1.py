
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        targetMap = collections.Counter(s1)
        charMap = collections.Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if charMap == targetMap:
                return True
            charMap[s2[i - len(s1)]] -= 1
            if charMap[s2[i - len(s1)]] == 0:
                del charMap[s2[i - len(s1)]]
            charMap[s2[i]] += 1

        return charMap == targetMap
