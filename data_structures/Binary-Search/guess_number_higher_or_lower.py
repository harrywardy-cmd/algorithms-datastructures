# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Set the initial search range from 1 to n.
        lower, upper = 1, n

        # Continue searching while the range is valid.
        while lower <= upper:

            # Find the middle number of the current search range.
            middle = (lower + upper) // 2

            # If the guessed number is too low,
            # search the upper half of the range.
            if guess(middle) > 0:
                lower = middle + 1

            # If the guessed number is too high,
            # search the lower half of the range.
            elif guess(middle) < 0:
                upper = middle - 1

            # If guess() returns 0, we found the correct number.
            else:
                return middle
