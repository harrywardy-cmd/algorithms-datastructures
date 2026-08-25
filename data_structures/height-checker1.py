class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Create a sorted version of the heights
        sortedHeights = sorted(heights)

        # Keep track of how many students are in the wrong position
        result = 0

        # Compare each student's current height with their expected height
        for i in range(len(heights)):
            # If the heights don't match, the student is out of position
            if heights[i] != sortedHeights[i]:
                result += 1

        # Return the total number of students in the wrong position
        return result
