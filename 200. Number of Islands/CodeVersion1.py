class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def dfs(coord):
            x, y = coord
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0" or coord in visited:
                return
            visited.add(coord)
            dfs((x - 1, y))  # Up
            dfs((x + 1, y))  # Down
            dfs((x, y - 1))  # Left
            dfs((x, y + 1))  # Right

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs((i, j))
        return islands
