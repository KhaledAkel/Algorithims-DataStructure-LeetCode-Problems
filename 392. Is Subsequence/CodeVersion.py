class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for char in t:
            if i == len(s):
                return True
            if char == s[i]:
                i += 1
        if i == len(s):
            return True
        return False
