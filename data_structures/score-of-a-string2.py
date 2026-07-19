class Solution:
    def scoreOfString(self, s: str) -> int:
        # Stores the total score of the string.
        res = 0

        # Iterate through each pair of adjacent characters.
        # We stop at len(s) - 1 because we'll compare s[i] with s[i + 1].
        for i in range(len(s) - 1):
            # Convert both characters to their ASCII values and
            # add the absolute difference to the running total.
            res += abs(ord(s[i]) - ord(s[i + 1]))

        # Return the final score.
        return res
