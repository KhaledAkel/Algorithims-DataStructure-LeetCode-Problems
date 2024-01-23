class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a,b = 0, 1

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        charSet = set([s[0]])
        out = 1
        
        while b<len(s): #
            while s[b] in charSet: # a b c
                charSet.remove(s[a])
                a += 1
            
            out = max(out, b-a+1)   # 3
            charSet.add(s[b]) 
            b += 1
        return out

                
            


        
