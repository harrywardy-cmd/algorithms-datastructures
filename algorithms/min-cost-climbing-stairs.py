class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Add a final step representing the "top" of the staircase.
        # Reaching the top has no additional cost.
        cost.append(0)

        # Work backwards through the staircase, starting from the
        # third-last element (since we look ahead by 1 and 2 steps).
        for i in range(len(cost) - 3, -1, -1):
            # Update the current step with the minimum total cost needed
            # to reach the top from this position.
            #
            # Option 1:
            #   Pay the current step's cost, then move to the next step.
            #
            # Option 2:
            #   Pay the current step's cost, then skip one step.
            #
            # Store the cheaper of the two options directly in the array,
            # turning the input list into a dynamic programming table.
            cost[i] = min(
                cost[i] + cost[i + 1],
                cost[i] + cost[i + 2]
            )

        # You can start from either step 0 or step 1.
        # Return the cheaper starting path.
        return min(cost[0], cost[1])
