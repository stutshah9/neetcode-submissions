class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # starting from the cell with the rottened fruit
        # if there are multiple rotten fruit treat all of them as starting points for the BFS algorithm
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        fresh = 0
        minute = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        # do BFS in all 4 directions
        while queue and fresh > 0:
            for _ in range(len(queue)):
                position = queue.popleft()
                x = position[0]
                y = position[1]
        # if there are fruits on any of the 4 directions they will rot in the next min
                # up
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    fresh -= 1
                    queue.append([x-1, y])
                # down
                if x < row - 1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    fresh -= 1
                    queue.append([x+1, y])
                # left
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    fresh -= 1
                    queue.append([x, y-1])
                # right
                if y < col - 1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    fresh -= 1
                    queue.append([x, y+1])
        # increment the min after each layer of the BFS
            minute += 1
        # by then end of the BFS algorithm is all the positions in the grid are either 0s or 2s then return the number of minutes it took
        # else return -1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        
        return minute