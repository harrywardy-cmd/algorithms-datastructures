class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Dictionary to count how many times each number appears.
        count = {}

        # Bucket array where the index represents the frequency.
        # Each bucket stores the numbers that appear that many times.
        # Maximum possible frequency is len(nums).
        freq = [[] for i in range(len(nums) + 1)]

        # Stores the final answer.
        res = []

        # Count the frequency of every number.
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Place each number into the bucket that matches its frequency.
        for num, c in count.items():
            freq[c].append(num)

        # Traverse the buckets from highest frequency to lowest.
        for i in range(len(freq) - 1, 0, -1):
            # Add every number in the current frequency bucket.
            for num in freq[i]:
                res.append(num)

                # Once we've collected k elements,
                # return the result immediately.
                if len(res) == k:
                    return res
