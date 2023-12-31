class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        lastAngram = None
        res = []

        for word in words:
            letters = [0]*26
            for letter in word:
                letters[ord(letter) - ord('a')] += 1
            if lastAngram != letters:
                lastAngram = letters
                res.append(word)
        return res

        
