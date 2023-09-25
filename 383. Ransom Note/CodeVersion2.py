class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for char in ransomNote:
            if char in magazine:
                ransomNote = ransomNote.replace(char, "", 1)
                magazine = magazine.replace(char,"", 1)
                if len(ransomNote) == 0:
                    return True
            else: 
                return False 
