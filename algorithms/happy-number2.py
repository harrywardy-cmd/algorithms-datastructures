class Solution:
    def isHappy(self, n: int) -> bool:
        # Initialize two pointers.
        # Slow moves one step at a time, fast moves two steps at a time.
        slow, fast = n, self.sumOfSquares(n)

        # Continue until the two pointers meet.
        while slow != fast:
            # Move the fast pointer forward by two steps.
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)

            # Move the slow pointer forward by one step.
            slow = self.sumOfSquares(slow)

        # If the cycle ends at 1, the number is happy.
        # Otherwise, it is trapped in a cycle.
        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        # Store the sum of the squared digits.
        output = 0

        # Process each digit in the number.
        while n:
            # Extract the last digit.
            digit = n % 10

            # Square the digit.
            digit = digit ** 2

            # Add it to the running total.
            output += digit

            # Remove the last digit.
            n = n // 10

        # Return the sum of squared digits.
        return output
