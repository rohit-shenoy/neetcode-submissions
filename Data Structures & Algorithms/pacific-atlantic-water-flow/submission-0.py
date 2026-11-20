class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        result = []

        def dfs(r, c, visit, prev_height):
            # check if in bounds, unvisited, and height flow
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                heights[r][c] < prev_height):
                return
            
            # otherwise can flow, visit and dfs neighbors
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # check first last rows
        for c in range(COLS):
            # marks can visit and explores neighbors
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS -1][c])


        # check first last cols
        for r in range(ROWS):
            # marks can visit and explores neighbors
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        return result
