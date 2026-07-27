class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        row, col = len(matrix), len(matrix[0])

        # Binary search across the rows
        top, bottom = 0, row - 1

        while top <= bottom:
            # Find the middle row
            curr_row = (top + bottom) // 2

            # If the target is greater than the last value in the row,
            # search the rows below
            if target > matrix[curr_row][-1]:
                top = curr_row + 1

            # If the target is smaller than the first value in the row,
            # search the rows above
            elif target < matrix[curr_row][0]:
                bottom = curr_row - 1

            # Otherwise, the target must be in this row (if it exists)
            else:
                break

        # If no valid row was found, the target doesn't exist
        if not top <= bottom:
            return False

        # Recalculate the row that may contain the target
        curr_row = (top + bottom) // 2

        # Perform a binary search within the selected row
        L, R = 0, col - 1

        while L <= R:
            # Find the middle column
            M = (L + R) // 2

            # If the target is larger, search the right half
            if target > matrix[curr_row][M]:
                L = M + 1

            # If the target is smaller, search the left half
            elif target < matrix[curr_row][M]:
                R = M - 1

            # Target found
            else:
                return True

        # Target was not found in the selected row
        return False
