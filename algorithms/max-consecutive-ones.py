class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Stores the longest streak of consecutive 1's found so far
        result = 0

        # Tracks the current streak of consecutive 1's
        count = 0

        # Loop through each number in the array
        for num in nums:
            # If the current number is 1, increase the streak by 1.
            # If it's 0, reset the streak back to 0.
            count = count + 1 if num else 0

            # Update the maximum streak if the current streak is larger
            result = max(result, count)

        # Return the longest consecutive sequence of 1's
        return result
