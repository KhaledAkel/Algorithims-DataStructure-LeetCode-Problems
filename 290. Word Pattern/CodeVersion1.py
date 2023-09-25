class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patt = []
        words = []

        for char in pattern:
            patt.append(pattern.index(char))
        split = list(s.split(" "))
        for word in split:
            words.append(split.index(word))

        if patt == words:
            return True
        else:
            return False
