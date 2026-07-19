class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge the first `m` sorted elements of nums1 with the first `n`
        sorted elements of nums2.

        The result is stored directly in nums1, as required by the problem.

        This solution:
        1. Replaces the unused portion of nums1 with the elements of nums2.
        2. Sorts nums1 to produce the final merged array.

        Time Complexity: O((m + n) log(m + n))
        Space Complexity: O(1) extra space (ignoring Python's internal sorting).
        """

        # Replace the unused portion of nums1 with all elements from nums2.
        nums1[m:] = nums2[:n]

        # Sort nums1 so that all elements are in ascending order.
        nums1.sort()

        """
        More Optimal Two-Pointer Solution (O(m + n))

        last = m + n - 1

        # Merge the arrays from the end so that we don't overwrite
        # values in nums1 that haven't been processed yet.
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # If any elements remain in nums2, copy them into nums1.
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        """
