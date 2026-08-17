class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Use a set to keep track of numbers that have appeared an odd
        # number of times.
        seen = set()

        # Go through each number in the array
        for num in nums:

            # If we've already seen the number, remove it.
            # This cancels out the previous occurrence.
            if num in seen:
                seen.remove(num)

            # If we haven't seen the number before, add it to the set.
            else:
                seen.add(num)

        # The only number left in the set is the number
        # that appeared exactly once.
        return list(seen)[0]
