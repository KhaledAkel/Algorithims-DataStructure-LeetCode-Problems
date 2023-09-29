class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        lis = list(s)  # Convert the input string to a list of characters

        while left < right:
            while left < right and lis[left] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                left += 1

            while left < right and lis[right] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                right -= 1
            
            if left < right:
                lis[left], lis[right] = lis[right], lis[left]
                left += 1
                right -= 1

        return "".join(lis)
