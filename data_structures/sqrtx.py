class Solution:
    def mySqrt(self, x: int) -> int:
        # Set the binary search boundaries.
        # The square root of x must be somewhere between 0 and x.
        L, R = 0, x

        # Stores the largest integer we've found whose square is <= x.
        result = 0

        # Continue searching while the boundaries are valid.
        while L <= R:
            # Find the middle value without risking integer overflow.
            mid = L + ((R - L) // 2)

            # If mid² is greater than x, mid is too large.
            # Search the left half.
            if mid**2 > x:
                R = mid - 1

            # If mid² is less than x, mid could be our answer.
            # Store it and search the right half for a larger value.
            elif mid**2 < x:
                L = mid + 1
                result = mid

            # If mid² equals x, we found the exact square root.
            else:
                return mid

        # If x isn't a perfect square, return the integer square root.
        return result
