class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create two hash maps:
        # mapST maps characters from s -> t
        # mapTS maps characters from t -> s
        mapST, mapTS = {}, {}

        # Compare each character at the same position
        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # Check for an inconsistent mapping:
            # 1. c1 was already mapped to a different character in t
            # 2. c2 was already mapped to a different character in s
            #
            # We need both checks to make sure the relationship
            # between the two strings is one-to-one.
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            # Store the mapping in both directions
            mapST[c1] = c2
            mapTS[c2] = c1

        # If every character has a consistent one-to-one mapping,
        # the strings are isomorphic.
        return True
