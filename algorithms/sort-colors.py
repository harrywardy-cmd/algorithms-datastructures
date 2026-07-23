class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Stores the count of each color:
        # Index 0 -> number of 0's (red)
        # Index 1 -> number of 1's (white)
        # Index 2 -> number of 2's (blue)
        colorCounts = [0, 0, 0]

        # First pass:
        # Count how many times each color appears
        for n in nums:
            colorCounts[n] += 1

        # Pointer used to overwrite the original array
        i = 0

        # Second pass:
        # Rebuild the array in sorted order
        for n in range(len(colorCounts)):
            # Write the current color as many times
            # as it appeared in the original array
            for j in range(colorCounts[n]):
                nums[i] = n
                i += 1
