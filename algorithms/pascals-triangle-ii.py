class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Start with the first row of Pascal's Triangle.
        current_row = [1]

        # Build each row until we reach the requested row.
        for _ in range(rowIndex):
            # Create the next row with one extra position.
            next_row = [0] * (len(current_row) + 1)

            # Each number in the current row contributes
            # to two adjacent positions in the next row.
            for index in range(len(current_row)):
                next_row[index] += current_row[index]
                next_row[index + 1] += current_row[index]

            # Move to the newly created row.
            current_row = next_row

        # Return the requested row.
        return current_row
