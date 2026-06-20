class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Store all valid triplets that sum to 0
        result = []

        # Sort the array so we can use the two-pointer technique
        nums.sort()

        # Iterate through each number, treating it as the first number in the triplet
        for i, a in enumerate(nums):

            # Skip duplicate values for the first number
            # This prevents duplicate triplets in the result
            if i > 0 and a == nums[i - 1]:
                continue

            # Initialize left and right pointers
            L, R = i + 1, len(nums) - 1

            # Search for two numbers that sum with 'a' to equal 0
            while L < R:
                threeSum = a + nums[L] + nums[R]

                # If sum is too large, move right pointer left
                # to reduce the total
                if threeSum > 0:
                    R -= 1

                # If sum is too small, move left pointer right
                # to increase the total
                elif threeSum < 0:
                    L += 1

                # Found a valid triplet
                else:
                    result.append([a, nums[L], nums[R]])

                    # Move both pointers inward
                    L += 1
                    R -= 1

                    # Skip duplicate values on the left pointer
                    # to avoid duplicate triplets
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        # Return all unique triplets that sum to 0
        return result
