class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        HashMap = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }

        if digits =="":
            return []
        
        result=[]
        def Combinning(digit, combination):
            if digit == len(digits):
                result.append(combination)
            else:
                for ch in HashMap[digits[digit]]:
                    Combinning(digit+1, combination + ch)
        Combinning(0, "")
        return result
