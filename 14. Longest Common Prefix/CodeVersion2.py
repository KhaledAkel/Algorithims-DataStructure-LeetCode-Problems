class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        l = 0
        pre = ""
        con = True
        
        while con:
            # We need to check if we are within bounds of all strings
            for i in range(len(strs)):
                if l >= len(strs[i]):
                    con = False
                    break
                if i == 0:
                    letter = strs[i][l]
                elif strs[i][l] != letter:
                    con = False
                    break
            if con:
                pre += letter
                l += 1

        return pre
