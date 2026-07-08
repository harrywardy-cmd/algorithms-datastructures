class Solution:
    def trap(self, height: List[int]) -> int:

        # Stores the total amount of trapped rainwater.
        result = 0

        # Only continue if the input list is not empty.
        if height:

            # Two pointers starting at the left and right ends.
            L, R = 0, len(height) - 1

            # Keep track of the tallest wall seen so far
            # from both the left and right sides.
            left_Max, right_Max = height[L], height[R]

            # Move the pointers toward each other.
            while L < R:

                # Process the side with the smaller maximum height,
                # since it determines the water level.
                if left_Max < right_Max:

                    # Move the left pointer inward.
                    L += 1

                    # Update the tallest wall seen from the left.
                    left_Max = max(left_Max, height[L])

                    # Water trapped at this position is the difference
                    # between the tallest left wall and the current height.
                    result += left_Max - height[L]

                else:

                    # Move the right pointer inward.
                    R -= 1

                    # Update the tallest wall seen from the right.
                    right_Max = max(right_Max, height[R])

                    # Water trapped at this position is the difference
                    # between the tallest right wall and the current height.
                    result += right_Max - height[R]

        # Return the total trapped rainwater.
        return result
