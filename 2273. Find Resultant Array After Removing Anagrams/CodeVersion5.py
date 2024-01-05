class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        stack = []
        for x in words:
            if len(stack) == 0:
                stack.append(x)
                continue
            if sorted(stack[-1]) != sorted(x):
                stack.append(x)
        return stack

            
