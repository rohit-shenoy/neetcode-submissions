class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Find correct row
        top, bot = 0, ROWS - 1

        # binary search for row
        while top <= bot:
            mid_row = top + ((bot - top) // 2)

            if target > matrix[mid_row][COLS - 1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                # found correct row - might exist here or not at all
                break

        # check if doesn't exist at all, immediately return false
        if top > bot:
            return False

        # correct row is:
        row = top + ((bot - top) // 2)

        # binary search within row
        l, r = 0, COLS - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        # didnt find
        return False