class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visit = set() # key: (r, c)

        def getAreaOfIsland(r: int, c: int) -> int:
            # base case
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or 
                grid[r][c] != 1 or 
                (r, c) in visit):
                return 0

            visit.add((r, c))

            return (1 + getAreaOfIsland(r + 1, c) + getAreaOfIsland(r - 1, c)
            + getAreaOfIsland(r, c + 1) + getAreaOfIsland(r, c - 1))



        for r in range(ROWS):
            for c in range(COLS):
                # new island
                if grid[r][c] == 1 and (r, c) not in visit:
                    currentArea = getAreaOfIsland(r, c)
                    maxArea = max(maxArea, currentArea)
        return maxArea
