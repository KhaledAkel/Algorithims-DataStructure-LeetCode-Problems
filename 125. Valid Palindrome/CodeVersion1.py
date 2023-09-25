class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''
        for char in s:
            if char.isalnum():
                alphanumeric += char.lower()
        
        n = len(alphanumeric)
        
        if n < 2:
            return True
        
        for i in range(n//2):
            if alphanumeric[i] != alphanumeric[-(i+1)]:
                return False
        
        return True
