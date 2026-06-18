import functools

class Solution:
    # Cache previously computed results so we don't
    # recalculate the same subproblems multiple times.
    @functools.lru_cache(None)
    def climbStairs(self, n: int) -> int:

        # Base cases:
        # If there is 1 step, there is 1 way to reach the top.
        # If there are 2 steps, there are 2 ways:
        # (1+1) or (2).
        if n == 2 or n == 1:
            return n

        # The number of ways to reach step n is the sum of:
        # - ways to reach step (n - 1) and take 1 step
        # - ways to reach step (n - 2) and take 2 steps
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
