class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Iterate through each character index of the first string
        # The first string is used as the reference for comparison
        for i in range(len(strs[0])):

            # Compare the current character with the same position
            # in every other string
            for s in strs:

                # If:
                # 1. We've reached the end of a string, or
                # 2. The characters do not match
                # then the common prefix ends before this index
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]

        # If all characters in the first string matched across
        # every string, then the entire first string is the prefix
        return strs[0]
