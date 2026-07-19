class Solution:
    def scoreOfString(self, s: str) -> int:
        # Convert each character in the string to its ASCII value.
        # Example: "hello" -> [104, 101, 108, 108, 111]
        ascii_values = [ord(char) for char in s]

        # Two pointers used to compare adjacent characters.
        i = 0
        j = 1

        # Stores the total score of the string.
        result = 0

        # Continue comparing adjacent characters until we reach the end.
        while j > i:

            # Stop once the second pointer moves beyond the last index.
            if j > len(ascii_values) - 1:
                break

            # Add the absolute difference between the two ASCII values.
            if ascii_values[j] >= ascii_values[i]:
                result += (ascii_values[j] - ascii_values[i])
            else:
                result += (ascii_values[i] - ascii_values[j])

            # Move both pointers to the next pair of adjacent characters.
            i += 1
            j += 1

        # Return the total score.
        return result
