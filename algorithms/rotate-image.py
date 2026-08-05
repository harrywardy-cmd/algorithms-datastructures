class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Initialize pointers for the current outer layer
        L, R = 0, len(matrix) - 1

        # Process one square layer at a time
        while L < R:
            # Rotate each element in the current layer
            for i in range(R - L):
                top, bottom = L, R

                # Save the top-left value since it will be overwritten
                topL = matrix[top][L + i]

                # Move bottom-left -> top-left
                matrix[top][L + i] = matrix[bottom - i][L]

                # Move bottom-right -> bottom-left
                matrix[bottom - i][L] = matrix[bottom][R - i]

                # Move top-right -> bottom-right
                matrix[bottom][R - i] = matrix[top + i][R]

                # Move saved top-left -> top-right
                matrix[top + i][R] = topL

            # Move inward to the next layer
            R -= 1
            L += 1
