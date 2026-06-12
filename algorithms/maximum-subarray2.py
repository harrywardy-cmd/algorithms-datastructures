class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the maximum sum with the first element.
        # This handles cases where all numbers are negative.
        maxSum = nums[0]

        # Current running sum of the subarray being considered.
        curSum = 0

        # Iterate through each number in the array.
        for n in nums:

            # If the current sum is negative, discard it and start fresh.
            # A negative sum would only reduce the total of any future subarray.
            curSum = max(curSum, 0)

            # Add the current number to the running sum.
            curSum += n

            # Update the maximum subarray sum found so far.
            maxSum = max(maxSum, curSum)

        # Return the largest subarray sum.
        return maxSum
