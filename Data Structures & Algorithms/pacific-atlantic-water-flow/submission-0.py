class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacVisited = set()
        atlVisited = set()

        res = []

        def dfs(r, c, visitSet, prevHeight):
            if (r,c) in visitSet or r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight:
                return 
            visitSet.add((r,c))
            dfs(r+1, c, visitSet, heights[r][c])
            dfs(r-1, c, visitSet, heights[r][c])
            dfs(r, c+1, visitSet, heights[r][c])
            dfs(r, c-1, visitSet, heights[r][c])

        # every column in the first row
        for c in range(COLS):
            dfs(0, c, pacVisited, heights[0][c])
            dfs(ROWS-1, c, atlVisited, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pacVisited, heights[r][0])
            dfs(r, COLS-1, atlVisited, heights[r][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacVisited and (r,c) in atlVisited:
                    res.append([r,c])
        
        return res
