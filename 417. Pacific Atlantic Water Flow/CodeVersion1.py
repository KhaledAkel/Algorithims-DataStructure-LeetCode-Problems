class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, reachable):
            reachable[r][c] = True
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)
        
        for i in range(rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, cols - 1, atlantic_reachable)
        
        for j in range(cols):
            dfs(0, j, pacific_reachable)
            dfs(rows - 1, j, atlantic_reachable)
        
        result = [[r, c] for r in range(rows) for c in range(cols) if pacific_reachable[r][c] and atlantic_reachable[r][c]]
        return result
