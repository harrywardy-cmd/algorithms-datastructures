class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Start Pascal's Triangle with the first row
        result = [[1]]

        # Generate the remaining rows
        for i in range(numRows - 1):
            # Pad the previous row with zeros on both sides
            # This makes it easy to calculate the next row
            # Example:
            # Previous row: [1, 2, 1]
            # Padded row:   [0, 1, 2, 1, 0]
            tempRow = [0] + result[-1] + [0]

            # Store the newly generated row
            row = []

            # Each value is the sum of two adjacent numbers
            # in the padded previous row
            for j in range(len(result[-1]) + 1):
                row.append(tempRow[j] + tempRow[j + 1])

            # Add the completed row to the triangle
            result.append(row)

        # Return the completed Pascal's Triangle
        return result
