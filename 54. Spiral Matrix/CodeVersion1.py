class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,t=0,0
        r = len(matrix[0])
        b = len(matrix)
        output = []

        while l < r and t < b:
            for i in range(l,r):
                output.append(matrix[t][i])
            t += 1

            for i in range(t,b):
                output.append(matrix[i][r-1])

            r -= 1

            if not (l< r and t < b):
                break

            for i in range(r-1,l-1,-1):
                output.append(matrix[b-1][i])
            b -= 1

            for i in range(b - 1, t- 1, -1):
                output.append(matrix[i][l])
            l += 1


        return output
