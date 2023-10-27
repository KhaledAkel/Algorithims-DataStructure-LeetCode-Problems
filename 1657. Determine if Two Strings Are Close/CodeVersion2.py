class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        occur1 = [word1.count(i) for i in set(word1)]
        occur2 = [word2.count(i) for i in set(word1)]
        
        for occur in occur1:
            if occur not in occur2: return False
            occur2.remove(occur)
        return True
