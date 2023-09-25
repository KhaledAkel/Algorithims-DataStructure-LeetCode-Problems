class Solution:
    def reverseWords(self, s: str) -> str:
        i, j = 0, 0
        newS = ""
        words = []
        word = ""
        while i < len(s):
            if s[i] != " ":
                j = i
                word = ""
                while j < len(s) and s[j] != " ":
                    word += s[j]
                    j += 1
                    i += 1
                words += [word]
            i += 1
        
        for i in range(len(words)-1, -1, -1):
            if i != 0:
                newS += words[i] + " "
            else:
                newS += words[i]
        return newS
