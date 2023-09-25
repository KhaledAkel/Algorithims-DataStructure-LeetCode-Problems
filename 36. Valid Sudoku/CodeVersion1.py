class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        lis = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    lis += [(i, num), (num, j), (i // 3, j // 3, num)]
        return len(lis) == len(set(lis))
