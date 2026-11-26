class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() # (r, c) = key
        numberOfIslands = 0

        def visitIsland(r, c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in visit or
                grid[r][c] == "0"):
                return
            
            # visit
            visit.add((r, c))

            # DFS neighbors
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                visitIsland(newR, newC)
            
        
        for r in range(ROWS):
            for c in range(COLS):
                # new island
                if (r, c) not in visit and grid[r][c] == "1":
                    numberOfIslands += 1
                    visitIsland(r, c)
        return numberOfIslands