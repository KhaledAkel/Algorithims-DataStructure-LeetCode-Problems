class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        HashMap = {}
        count = 0

        for letter in magazine:
            if letter not in HashMap.keys():
                HashMap[letter] = 0
            HashMap[letter] += 1

        for char in ransomNote:
            if char in HashMap.keys():
                HashMap[char] -= 1
                if HashMap[char] >= 0:
                    count += 1

        return True if count == len(ransomNote) else False
