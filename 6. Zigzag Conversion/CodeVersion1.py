class Solution:
    def convert(self, s: str, numRows: int) -> str:
        switch,j, count = 0,0,0
        zigzag = [[] for _ in range(numRows)]
        result = ""
        if len(s) <=1 or numRows <= 1:
            return s
        for i in range(len(s)):
            if count == numRows:
                count = 1
                if switch == 0:
                    switch = 1
                    j = -2
                else:
                    switch = 0
                    j = 1
            
            if switch == 0:
                zigzag[j] += [s[i]]
                j += 1
                count +=1
            else:
                zigzag[j] += [s[i]]
                j -= 1
                count +=1
        for i in range(numRows):
            result += "".join(zigzag[i])

        return result 
