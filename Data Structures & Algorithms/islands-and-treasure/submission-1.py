class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() # already calculated
        q = collections.deque()

        # add all treasures to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))


        def visitCell(r, c):
            # check conditions
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] == -1 or
                (r, c) in visit):
                return

            # mark as visited
            visit.add((r, c))

            # append to queue - continue from this for next layer
            q.append((r, c))

        dist = 0
        # Simultaneous BFS from all (mark one layer at a time)
        while q:
            # all cells at dist from treasure
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                visitCell(r + 1, c)
                visitCell(r - 1, c)
                visitCell(r, c + 1)
                visitCell(r, c - 1)
            # increment layer
            dist += 1
