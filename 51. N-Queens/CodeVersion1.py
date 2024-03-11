class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(row, col, taken):
            if row in taken['row'] or col in taken['col']:
                return False

            for i, j in taken['pos']:
                if abs(row - i) == abs(col - j):
                    return False

            return True
        
        def backtrack(row, taken):
            if row == n:
                # All queens are placed successfully
                solutions.append(taken['pos'][:])  # Append a copy of the current positions
                return
            
            for col in range(n):
                if isValid(row, col, taken):
                    # Place the queen
                    taken['row'].add(row)
                    taken['col'].add(col)
                    taken['pos'].append((row, col))

                    # Move to the next row
                    backtrack(row + 1, taken)

                    # Remove the queen if the solution is not valid
                    taken['row'].remove(row)
                    taken['col'].remove(col)
                    taken['pos'].pop()

        solutions = []
        taken = {'row': set(), 'col': set(), 'pos': []}
        backtrack(0, taken)
        
        # Format solutions as a list of lists of strings
        result = []
        for solution in solutions:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for i, j in solution:
                board[i][j] = 'Q'
            result.append([''.join(row) for row in board])

        return result
