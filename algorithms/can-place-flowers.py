class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Keep track of how many flowers we can successfully plant
        count = 0

        # Add empty spaces to both ends of the flowerbed.
        # This makes it easier to check the neighbours of the first
        # and last positions without needing special cases.
        temp = [0] + flowerbed + [0]

        # Check each position, excluding the added boundary zeros
        for i in range(1, len(temp) - 1):

            # A flower can only be planted if the current spot is empty
            if temp[i] == 0:

                # Check that both neighbouring spots are also empty
                if temp[i - 1] == 0 and temp[i + 1] == 0:

                    # Plant a flower here
                    count += 1
                    temp[i] = 1

        # Return True if we were able to plant at least n flowers
        return count >= n
