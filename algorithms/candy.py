class Solution:
    def candy(self, ratings: List[int]):

        # Give every child one candy to satisfy the minimum requirement.
        candies = [1] * len(ratings)

        # Pass 1: Traverse from right to left.
        # If the current child has a higher rating than the child to the right,
        # they must receive more candies than their right neighbor.
        for child in range(len(ratings) - 1, -1, -1):
            if child + 1 in range(len(ratings)):
                if ratings[child] > ratings[child + 1]:
                    candies[child] = max(candies[child], candies[child + 1] + 1)

        # Pass 2: Traverse from left to right.
        # If the current child has a higher rating than the child to the left,
        # they must receive more candies than their left neighbor.
        # We use max() so we don't overwrite a larger value assigned
        # during the first pass.
        for child in range(len(ratings)):
            if child - 1 in range(len(ratings)):
                if ratings[child] > ratings[child - 1]:
                    candies[child] = max(candies[child], candies[child - 1] + 1)

        # Return the minimum total number of candies needed.
        return sum(candies)
