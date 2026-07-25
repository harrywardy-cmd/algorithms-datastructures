class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum possible eating speed is 1 banana per hour.
        # The maximum possible eating speed is the size of the largest pile.
        L, R = 1, max(piles)

        # Store the best (smallest valid) eating speed found so far.
        result = R

        # Binary search for the minimum valid eating speed.
        while L <= R:
            # Test the middle eating speed.
            k = (L + R) // 2

            # Calculate how many hours Koko would need
            # to eat all banana piles at speed k.
            hours = 0

            for p in piles:
                # Each pile takes the ceiling of (pile size / speed)
                # because Koko cannot partially spend an hour.
                hours += math.ceil(p / k)

            # If Koko can finish within the allowed hours,
            # this speed works. Try finding a slower valid speed.
            if hours <= h:
                result = min(result, k)
                R = k - 1

            # Otherwise, the speed is too slow.
            # Search the faster half.
            else:
                L = k + 1

        # Return the minimum valid eating speed.
        return result
