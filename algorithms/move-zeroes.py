class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Left pointer tracks the position where the next
        # non-zero element should be placed.
        l = 0

        # Right pointer scans through every element in the array.
        for r in range(len(nums)):

            # If the current element is non-zero...
            if nums[r]:

                # Swap the current non-zero element with the element
                # at the left pointer. If l == r, this swap does nothing.
                nums[l], nums[r] = nums[r], nums[l]

                # Move the left pointer forward to the next position
                # where a non-zero element should be placed.
                l += 1
