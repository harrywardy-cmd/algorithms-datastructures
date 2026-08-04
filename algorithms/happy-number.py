class Solution:
    def isHappy(self, n: int) -> bool:
        # Store numbers we've already seen to detect a cycle.
        visit = set()

        # Continue until we either reach 1 or repeat a number.
        while n not in visit:
            # Mark the current number as visited.
            visit.add(n)

            # Replace the number with the sum of the squares of its digits.
            n = self.sumOfSquares(n)

            # If we reach 1, the number is happy.
            if n == 1:
                return True

        # We entered a cycle without reaching 1, so the number is not happy.
        return False

    def sumOfSquares(self, n: int) -> int:
        # Store the running total of squared digits.
        output = 0

        # Process each digit until no digits remain.
        while n:
            # Get the last digit.
            digit = n % 10

            # Square the digit.
            digit = digit ** 2

            # Add the squared digit to the total.
            output += digit

            # Remove the last digit from the number.
            n = n // 10

        # Return the sum of the squared digits.
        return output
