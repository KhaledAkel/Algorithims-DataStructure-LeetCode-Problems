class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if needle == haystack[i:i+length]:
                    return i
        return -1
