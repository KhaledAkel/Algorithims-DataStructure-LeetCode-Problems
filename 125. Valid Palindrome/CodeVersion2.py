class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = []
        for char in s:
            if char.isalnum():
                lis.append(char.lower())
        return "".join(lis) == "".join(lis[::-1])
