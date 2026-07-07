class Solution:
    def climbStairs(self, n: int) -> int:

        # Cache stores the number of ways to reach the top from each step.
        # -1 means we haven't calculated that position yet.
        cache = [-1] * n

        def dfs(i):
            # If we've gone past the last step, this path is invalid.
            if i > n:
                return 0

            # If we've landed exactly on the top step,
            # we've found one valid way to climb the stairs.
            if i == n:
                return 1

            # If we've already calculated this subproblem,
            # return the stored result instead of recomputing it.
            if cache[i] != -1:
                return cache[i]

            # The number of ways from the current step is:
            #   ways by taking 1 step
            # + ways by taking 2 steps
            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]

        # Start climbing from step 0.
        return dfs(0)
