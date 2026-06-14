class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Stores the index of the last non-space character
        R = 0

        # Tracks the length of the last word
        result = 0

        # Scan from right to left to find the end of the last word.
        # This skips any trailing spaces at the end of the string.
        for x in range(len(s) - 1, -1, -1):
            if s[x] != " ":
                R = x
                break

        # Starting from the last character of the last word,
        # move left until a space is found.
        # Count each character to determine the word length.
        for y in range(R, -1, -1):
            if s[y] != " ":
                result += 1
            else:
                break

        # Return the length of the last word.
        return result
