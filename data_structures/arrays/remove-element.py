class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer indicating the position where the next
        # valid (non-val) element should be placed.
        k = 0

        # Iterate through every element in the array.
        for i in range(len(nums)):
            # If the current element is not the value to remove...
            if nums[i] != val:
                # Copy the current element to the next available position.
                nums[k] = nums[i]

                # Move the insertion pointer forward.
                k += 1

        # Return the number of elements that remain after removal.
        # The first k elements of nums contain the valid values.
        return k
