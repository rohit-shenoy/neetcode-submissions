class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # use hashmaps for each row, column, and square
        rows = collections.defaultdict(set) # key: r
        cols = collections.defaultdict(set) # key: c
        squares = collections.defaultdict(set) # key: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                # neat trick: integer divide rows & cols (0-9) to 0,1,2 squares
                squares[(r // 3, c // 3)].add(board[r][c])
        return True