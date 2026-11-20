class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        number_of_islands = 0
        visited = set()  # key: (r, c)
        ROWS, COLS = len(grid), len(grid[0])

        # Graph traversal helper func. to mark layers of 1s as visited
        def bfs(r: int, c: int) -> None:

            # mark as visited and add to q
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()  # FIFO
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # check in bounds, if it's 1, and not visited
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and grid[new_row][new_col] == "1"
                        and (new_row, new_col) not in visited
                    ):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        # Iterate
        for r in range(ROWS):
            for c in range(COLS):
                # unvisited new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    # do bfs on it and mark it visited, increment count
                    bfs(r, c)
                    number_of_islands += 1
        return number_of_islands