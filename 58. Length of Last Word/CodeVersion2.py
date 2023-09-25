class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Solving without using Built in Function like .split()
        words=[]
        pointer=0
        for i in range(len(s)):
            if s[i] == " ":
                if len(s[pointer:i]) != 0:
                    words += [s[pointer:i]]
                pointer = i+1
        if s[-1] != " ":
            words += [s[pointer::]]
        if len(words) == 0:
            return len(s)
        else:
            return len(words[-1])
