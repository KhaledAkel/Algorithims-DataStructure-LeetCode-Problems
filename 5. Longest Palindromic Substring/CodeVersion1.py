class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        
        maxLen = 1
        maxStr = s[0]

        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if (j-i+1) > maxLen and s[i:j+1] == s[i:j+1][::-1]:
                    maxLen = len(s[i:j+1])
                    maxStr = s[i:j+1]
        return maxStr
        
