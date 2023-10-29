class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rowsMap = Counter([tuple(lis) for lis in grid])
        count = 0

        for i in range(len(grid)):
            col = tuple([grid[j][i] for j in range(len(grid)) ])
            if col in rowsMap:
                count += rowsMap[col]

        return count





        
