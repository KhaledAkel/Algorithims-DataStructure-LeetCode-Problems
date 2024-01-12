class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in Map:
                if stack and stack[-1] != Map[char]:
                    return False
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        
        return len(stack) == 0        
