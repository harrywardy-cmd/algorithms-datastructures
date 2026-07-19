class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # Keeps track of the greatest element to the right of the current index.
        # The last element has no elements to its right, so it will become -1.
        highest = -1

        # Traverse the array from right to left.
        for i in range(len(arr) - 1, -1, -1):
            # Store the current value before overwriting it.
            current = arr[i]

            # Replace the current element with the greatest value
            # seen so far to its right.
            arr[i] = highest

            # Update the greatest value if the current element is larger.
            highest = max(highest, current)

        # Return the modified array.
        return arr
