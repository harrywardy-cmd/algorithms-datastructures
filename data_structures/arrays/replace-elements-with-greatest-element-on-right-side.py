class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # Keeps track of the greatest element to the right
        # of the current index. The last element will become -1.
        highest = -1

        # Temporarily stores the current value before it is overwritten.
        temp = 0

        # Start from the last element and move left.
        i = len(arr) - 1

        # Traverse the array from right to left.
        while i >= 0:

            # If the current element is greater than the highest value
            # we've seen so far, update the highest value.
            if arr[i] > highest:
                # Save the current value before overwriting it.
                temp = arr[i]

                # Replace the current element with the greatest value
                # to its right.
                arr[i] = highest

                # Update the highest value for future iterations.
                highest = temp

            else:
                # Otherwise, simply replace the current element
                # with the greatest value found so far.
                arr[i] = highest

            # Move to the previous element.
            i -= 1

        # Return the modified array.
        return arr
            
