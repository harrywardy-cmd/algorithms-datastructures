class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Left and right pointers define the current search range.
        L, R = 0, len(nums) - 1

        # Continue searching while the search range is valid.
        while L <= R:
            # Find the middle index of the current range.
            M = (L + R) // 2

            # If the target is greater than the middle value,
            # search the right half.
            if target > nums[M]:
                L = M + 1

            # If the target is less than the middle value,
            # search the left half.
            elif target < nums[M]:
                R = M - 1

            # Target found, return its index.
            else:
                return M

        # Target was not found in the array.
        return -1
