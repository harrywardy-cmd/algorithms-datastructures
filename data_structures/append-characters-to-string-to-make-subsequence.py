class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Pointer for string t.
        # Tracks the next character in t that we are trying to match.
        j = 0

        # Iterate through each character in s.
        for i in range(len(s)):

            # Ensure j is still within the bounds of t.
            # Once all characters in t have been matched,
            # there is no need to continue matching.
            if j < len(t):

                # If the current character in s matches the
                # current target character in t, move to the
                # next character in t.
                if t[j] == s[i]:
                    j += 1

        # j represents the number of characters from t
        # that were successfully matched as a subsequence of s.
        # The remaining characters need to be appended to s.
        return len(t) - j
