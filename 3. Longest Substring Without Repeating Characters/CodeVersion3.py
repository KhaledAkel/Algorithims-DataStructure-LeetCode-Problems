class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest = 0
        visited = set()
        i, j  = 0, 0 
        while i < len(s) and j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                j += 1
                longest = max(longest, j-i)
            else:
                visited.remove(s[i])
                i += 1
        return longest




