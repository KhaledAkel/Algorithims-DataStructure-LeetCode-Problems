class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        i=0
        HashMap = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        while i < len(s)-1:

                if s[i] == "I" and ((s[i+1] == "V") or(s[i+1] == "X")):
                    result += HashMap[s[i] + s[i+1]]
                    i += 2
                elif s[i] == "X" and ((s[i+1] == "L") or(s[i+1] == "C")):
                    result += HashMap[s[i] + s[i+1]]
                    i += 2
                elif s[i] == "C" and ((s[i+1] == "D") or(s[i+1] == "M")):
                    result += HashMap[s[i] + s[i+1]]
                    i += 2
                else:
                    result += HashMap[s[i]]
                    i += 1
        if i == len(s)-1:
            result += HashMap[s[i]]
            i += 1

        return result
