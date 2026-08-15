class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # begin by finding all the island using DFS
        # have a counter at the first square of the island
        # DFs through the island
        # if there is a 1 at the same place for other island keep going
        # if there isn't they are not the same island and the other island must be checked
        # can do this with a set and save the path of the island so it does not need to be retraced
        # save he relative coordinates not the exact coordinates
        # once the position on the grid has been visited change it to 0

        pathSet = set()

        row = len(grid)
        col = len(grid[0])

        unique = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    pathList = []
                    startPoint = (i, j)
                    self.DFS(grid, i, j, pathList, startPoint)

                    if tuple(pathList) not in pathSet:
                        unique += 1
                        pathSet.add(tuple(pathList))
        
        return unique

    # DFS function to return the relative path of the islands to add to the set
    def DFS(self, grid, row, col, pathList, startPoint):
        # change the value to visited
        grid[row][col] = 0
        pathList.append((startPoint[0] - row, startPoint[1] - col))

        # left
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            self.DFS(grid, row, col - 1, pathList, startPoint)

        # right
        if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
            self.DFS(grid, row, col + 1, pathList, startPoint)

        # up
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            self.DFS(grid, row - 1, col, pathList, startPoint)

        # down
        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            self.DFS(grid, row + 1, col, pathList, startPoint)