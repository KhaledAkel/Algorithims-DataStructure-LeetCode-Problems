class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, block, r, c, val):
            block_index = (r // 3) * 3 + (c // 3)
            if val in row[r] or val in col[c] or val in block[block_index]:
                return False
            return True

        def placeNumber(board, row, col, block, r, c, val):
            board[r][c] = val
            row[r].add(val)
            col[c].add(val)
            block[(r // 3) * 3 + (c // 3)].add(val)

        def removeNumber(board, row, col, block, r, c, val):
            board[r][c] = '.'
            row[r].remove(val)
            col[c].remove(val)
            block[(r // 3) * 3 + (c // 3)].remove(val)

        def backtrack(board, row, col, block):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            if isValid(row, col, block, i, j, str(num)):
                                placeNumber(board, row, col, block, i, j, str(num))
                                if backtrack(board, row, col, block):
                                    return True
                                removeNumber(board, row, col, block, i, j, str(num))
                        return False
            return True

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [set() for _ in range(9)]

   
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = board[i][j]
                    row[i].add(val)
                    col[j].add(val)
                    block[(i // 3) * 3 + (j // 3)].add(val)

        backtrack(board, row, col, block)
