class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        output = 0
        vowelsSet = {'a', 'e', 'i', 'o', 'u'}

        for j in range(k):
            if s[j] in vowelsSet:
                output += 1

        copy = output
        for i in range(k, len(s)):
            if s[i-k] in vowelsSet:
                copy -= 1
            if s[i] in vowelsSet:
                copy += 1
            
            output = max(copy, output)
        return output
        
