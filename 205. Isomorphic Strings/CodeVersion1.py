class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        word1, word2 = [], []

        for char in s:
            word1.append(s.index(char))
        for char in t:
            word2.append(t.index(char))

        if word1 == word2:
            return True
        return False
