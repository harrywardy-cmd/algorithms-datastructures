class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Track the length of the current increasing subarray
        increase = 1

        # Track the length of the current decreasing subarray
        decreasing = 1

        # Store the longest monotonic subarray found so far
        result = 1

        # Start from the second element and compare it with the previous element
        for i in range(1, len(nums)):

            # Equal values break both increasing and decreasing sequences
            if nums[i] == nums[i - 1]:
                increase = 1
                decreasing = 1

            # Current value is greater than the previous value,
            # so we can extend the increasing sequence
            elif nums[i] > nums[i - 1]:
                increase = increase + 1

                # Increasing means the decreasing sequence is broken
                decreasing = 1

            # Current value is smaller than the previous value,
            # so we can extend the decreasing sequence
            else:
                # Decreasing means the increasing sequence is broken
                increase = 1
                decreasing = decreasing + 1

            # Keep track of the longest increasing or decreasing
            # subarray found so far
            result = max(result, increase, decreasing)

        # Return the length of the longest monotonic subarray
        return result
