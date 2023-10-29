class Solution:
    def removeStars(self, s: str) -> str:

        delStars = 0
        toBeRemoved = set()

        for i in range(len(s)-1,-1,-1):
            if s[i] == "*":
                delStars += 1
                toBeRemoved.add(i)
            else:
                if delStars > 0:
                    toBeRemoved.add(i)
                    delStars -= 1

        return ''.join([s[i] for i in range(len(s)) if i not in toBeRemoved])


                    
