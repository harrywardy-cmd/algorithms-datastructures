class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Dictionary to store how many times each number appears.
        seen = {}

        # Loop through every number in the array.
        for i in range(len(nums)):

            # If this number hasn't been seen before,
            # add it to the dictionary with an initial count of 0.
            if nums[i] not in seen:
                seen[nums[i]] = 0

            # If we've already seen the number, increase its count.
            else:
                seen[nums[i]] = seen[nums[i]] + 1

        # Find the number with the highest count.
        max_key = max(seen, key=seen.get)

        # Return the number that appeared most frequently.
        return max_key
