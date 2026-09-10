class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Store the largest ascending sum found so far.
        # Start with the first number in the array.
        result = nums[0]

        # Store the sum of the current ascending subarray.
        cur = nums[0]

        # Start from the second element and compare it with the previous one.
        for i in range(1, len(nums)):

            # If the current number is not greater than the previous number,
            # the ascending sequence is broken, so start a new sum.
            if nums[i] <= nums[i - 1]:
                cur = 0

            # Add the current number to the current ascending sum.
            cur += nums[i]

            # Update the maximum sum if the current ascending sum is larger.
            result = max(result, cur)

        # Return the largest ascending subarray sum.
        return result
