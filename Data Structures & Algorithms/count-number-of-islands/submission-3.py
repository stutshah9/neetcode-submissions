class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        islandCount = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    islandCount += 1
                    self.DFS(i, j, grid, row, col)
        
        return islandCount

    def DFS(self, i, j, grid: List[List[str]], row, col) -> None:
        if i >= 0 and i < row and j >= 0 and j < col:
            if grid[i][j] == "1":
                grid[i][j] = "0"

                self.DFS(i-1, j, grid, row, col)
                self.DFS(i+1, j, grid, row, col)
                self.DFS(i, j-1, grid, row, col)
                self.DFS(i, j+1, grid, row, col)
        