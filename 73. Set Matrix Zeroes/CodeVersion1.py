class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = set()
        row = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    col.add(j)
                    row.add(i)
        
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j]=0
