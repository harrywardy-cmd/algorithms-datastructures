class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Left pointer starts at the beginning of the array.
        L = 0

        # Right pointer starts at the end of the array.
        R = len(heights) - 1

        # Stores the maximum area found so far.
        res = 0

        # Continue until the two pointers meet.
        while L < R:
            # The height of the container is limited by the shorter line.
            # The width is the distance between the two pointers.
            area = min(heights[L], heights[R]) * (R - L)

            # Update the maximum area if the current container is larger.
            res = max(res, area)

            # Move the pointer with the shorter height inward.
            # This is the only way we have a chance of finding
            # a larger area, since the width is decreasing.
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        # Return the largest area found.
        return res
