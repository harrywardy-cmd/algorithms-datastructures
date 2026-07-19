class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the maximum sum with the first element.
        maxSum = nums[0]

        # Choose each index as the starting point of a subarray.
        for i in range(len(nums)):
            # Stores the sum of the current subarray.
            curSum = 0

            # Extend the subarray one element at a time.
            for j in range(i, len(nums)):
                # Add the current element to the running sum.
                curSum += nums[j]

                # Update the maximum subarray sum if the current
                # subarray produces a larger sum.
                maxSum = max(maxSum, curSum)

        # Return the largest subarray sum found.
        return maxSum
