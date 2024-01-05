class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = collections.defaultdict(int)
        for letter in s:
            letters[letter] += 1
        
        for letter in t:
            if letter in s and letters[letter] > 0:
                letters[letter] -= 1
                if letters[letter] == 0:
                    del letters[letter]

            else:
                return False
        return True if len(letters) == 0 else False
        
