class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lis1 = [i for i in s]
        lis2 = [i for i in t]
        lis1.sort()
        lis2.sort()

        if lis1 == lis2:
            return True
        else:
            return False
