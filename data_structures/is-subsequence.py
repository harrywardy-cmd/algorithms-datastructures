class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointer for string t
        i = 0

        # Pointer for string s (the subsequence we're trying to match)
        j = 0

        # Traverse through both strings
        while i < len(t) and j < len(s):

            # If the current characters match,
            # move to the next character in s
            if t[i] == s[j]:
                j += 1

            # Always move to the next character in t
            i += 1

        # If we've matched every character in s,
        # then s is a subsequence of t
        return j == len(s)
