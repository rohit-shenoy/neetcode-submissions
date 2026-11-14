class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        numberOfIslands = 0
        visit = set() # key = (r, c)

        def visitIsland(r, c):
            # check if in bounds and unvisited and land
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or 
                (r, c) in visit or 
                grid[r][c] == "0"):
                return 

            # if yes, then visit it
            visit.add((r, c))

            # visit using dfs its neighbors
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dirR, dirC in neighbors:
                newR, newC = r + dirR, c + dirC
                visitIsland(newR, newC)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    visitIsland(r, c)
                    numberOfIslands += 1
        return numberOfIslands