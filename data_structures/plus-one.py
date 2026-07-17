class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Get the number of digits in the array.
        n = len(digits)

        # Traverse the number from right to left (least significant digit first).
        for i in range(n - 1, -1, -1):

            # If the current digit is less than 9,
            # simply increment it and return the result.
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If the current digit is 9,
            # adding 1 causes it to roll over to 0
            # and carry the 1 to the next digit.
            digits[i] = 0

        # If we reach here, every digit was a 9.
        # Example:
        # [9]      -> [1, 0]
        # [9,9]    -> [1,0,0]
        # [9,9,9]  -> [1,0,0,0]
        return [1] + digits
