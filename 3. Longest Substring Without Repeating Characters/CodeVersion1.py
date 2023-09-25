class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left ,length = 0,0
        Set = set()
        for i in range(len(s)):
            while s[i] in Set:
                Set.remove(s[left])
                left+=1
            Set.add(s[i])
            length = max(length, i-left+1)
        return length
