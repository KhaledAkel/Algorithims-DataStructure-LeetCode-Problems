class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islandArea, visited = 0, set()

        def dfs(i,j):
            if (i<0 or i>len(grid)-1 or
                j<0 or j >len(grid[0])-1 or
                grid[i][j] == 0 or (i,j) in visited):
                return 0
            
            visited.add((i,j))
            area = 1
            area += dfs(i+1,j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i,j-1)

            return area 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                islandArea = max(islandArea, dfs(i,j))
        return islandArea
        
