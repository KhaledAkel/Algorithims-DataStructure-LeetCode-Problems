
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]
        for i in range(len(strs[0])):
            comp = strs[0][i]
            for j in range(1, n):
                if i == len(strs[j]) or comp != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
        
