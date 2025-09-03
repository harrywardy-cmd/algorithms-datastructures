class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        length = 0
        L = 0

        for R in range(len(s)):
            while s[R] in string:
                string.remove(s[L])
                L += 1
            string.add(s[R])
            length = max(R - L + 1, length)

        return length
            
