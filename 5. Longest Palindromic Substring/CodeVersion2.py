class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        maxStr = s[0]

        def expand(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)-1):
            odd = expand(i,i)
            even = expand(i, i+1)

            if len(odd) > len(maxStr):
                maxStr = odd
            if len(even) > len(maxStr):
                maxStr = even
            
        return maxStr
