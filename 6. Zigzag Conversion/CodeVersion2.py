class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        matrix = [[] for _ in range(numRows)]
        i = 0
        direction = 1  # 1 for down, -1 for up

        for char in s:
            matrix[i].append(char)
            if i == 0:
                direction = 1
            elif i == numRows - 1:
                direction = -1
            i += direction

     
        converted_string = ''.join([''.join(row) for row in matrix])
        return converted_string
