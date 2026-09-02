class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Store the index of each number in nums1
        nums1Temp = {num: i for i, num in enumerate(nums1)}

        # Start every answer as -1
        ans = [-1] * len(nums1)

        # Go through each number in nums2
        for i in range(len(nums2)):

            # Skip numbers that are not in nums1
            if nums2[i] not in nums1Temp:
                continue

            # Look for the next greater number to the right
            for j in range(i + 1, len(nums2)):
                
                # If we find a greater number, update the answer
                if nums2[j] > nums2[i]:
                    temp = nums1Temp[nums2[i]]
                    ans[temp] = nums2[j]
                    break

        # Return the next greater elements for nums1
        return ans
