class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        # helper uses BFS to explore island, mark visited, and returns area
        def bfs(r: int, c: int) -> int:
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            current_area = 1

            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # check if in bounds, unvisited, and a 1, then increment area and continue exploring its neighbors
                    if (
                        new_row in range(ROWS)
                        and new_col in range(COLS)
                        and grid[new_row][new_col] == 1
                        and (new_row, new_col) not in visited
                    ):
                        current_area += 1
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

            return current_area

        # Iterate and find a new island
        for r in range(ROWS):
            for c in range(COLS):
                # new island
                if grid[r][c] == 1 and (r, c) not in visited:
                    # do bfs and get area
                    area_of_island = bfs(r, c)
                    max_area = max(max_area, area_of_island)
        return max_area