class Solution:
    def maxDifference(self, s: str) -> int:
        # Count how many times each character appears in the string
        count = Counter(s)

        # Track the largest odd frequency and smallest even frequency
        oddMax, evenMin = 0, len(s)

        # Check the frequency of each character
        for i in count.values():
            # If the frequency is odd, update the maximum odd frequency
            if i & 1:
                oddMax = max(oddMax, i)
            # If the frequency is even, update the minimum even frequency
            else:
                evenMin = min(evenMin, i)

        # Return the difference between the largest odd
        # frequency and the smallest even frequency
        return oddMax - evenMin
