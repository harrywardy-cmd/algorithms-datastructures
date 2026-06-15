class Solution:
    def confusingNumber(self, n: int) -> bool:
        # Mapping of digits to their rotated counterparts.
        # Digits not present in this dictionary are invalid when rotated.
        validNum = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        # Stores the rotated digits as we build the new number.
        rotated_number = []

        # Iterate through each digit in the original number.
        for char in str(n):
            # If the digit cannot be rotated, the number is not confusing.
            if char not in validNum:
                return False

            # Append the rotated version of the current digit.
            rotated_number.append(validNum[char])

        # Convert the list of rotated digits into a string.
        rotated_number = "".join(rotated_number)

        # Reverse the rotated number to simulate a 180-degree rotation.
        # A number is confusing if the rotated result differs from the original.
        return int(rotated_number[::-1]) != n
