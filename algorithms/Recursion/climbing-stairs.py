import functools

class Solution:
    @functools.lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 1:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
