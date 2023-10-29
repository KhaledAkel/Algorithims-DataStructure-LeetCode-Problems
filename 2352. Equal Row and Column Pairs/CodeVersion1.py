class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            lis = [grid[j][i] for j in range(len(grid)) ]
            for row in grid:
                if lis == row:
                    count += 1

        return count





        
