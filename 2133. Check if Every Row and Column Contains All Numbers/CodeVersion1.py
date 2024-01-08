class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        for i in range(len(matrix)):
            row = []
            col = []
            for j in range(len(matrix)):
                row.append(matrix[i][j])
                col.append(matrix[j][i])

            if len(set(row)) != len(matrix) or len(set(col)) != len(matrix):
                return False
        return True 

        
