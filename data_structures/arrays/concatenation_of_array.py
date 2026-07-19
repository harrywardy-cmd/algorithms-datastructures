class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Stores the concatenated result.
        ans = []

        # Repeat the process twice to create nums + nums.
        for i in range(2):
            # Append every element from the original array.
            for num in nums:
                ans.append(num)

        # Return the concatenated array.
        return ans
