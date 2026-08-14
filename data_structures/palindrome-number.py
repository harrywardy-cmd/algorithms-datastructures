class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        # Find the highest place value (e.g., for 12321, d = 10000)
        d = 1
        while x >= 10 * d:
            d *= 10

        # Compare the first and last digits
        while x:
            # If the first digit and last digit are different,
            # the number is not a palindrome
            if x // d != x % 10:
                return False

            # Remove the first and last digits
            x = (x % d) // 10

            # Move to the next pair of digits
            d //= 100

        # All digit pairs matched
        return True
