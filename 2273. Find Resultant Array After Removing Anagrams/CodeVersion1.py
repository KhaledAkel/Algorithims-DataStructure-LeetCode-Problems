class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        SET = set()
        res = []
        prev = None

        for word in words:
            letters = [0]*26
            for letter in word:
                letters[ord(letter)- ord('a')] += 1
            if tuple(letters) not in SET:
                res.append(word)
                SET.add(tuple(letters))
            if (prev != None) and (prev != letters):
                SET.remove(tuple(prev))
            prev = letters
        return res


        
