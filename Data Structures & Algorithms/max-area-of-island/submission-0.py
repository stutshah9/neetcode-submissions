class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if the grid is empty there are no island to meansure the area of
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])

        maxArea = 0

        def dfs(row, col) -> int:
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea