class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The goal starts at the last index because
        # that is the position we ultimately want to reach.
        goal = len(nums) - 1

        # Traverse the array from right to left.
        # At each index, check whether we can jump
        # to the current goal (or beyond it).
        for i in range(len(nums) - 1, -1, -1):

            # If the maximum jump from this position
            # reaches the current goal, then this index
            # becomes the new goal.
            if (i + nums[i]) >= goal:
                goal = i

        # If we were able to move the goal all the way
        # back to index 0, then we can reach the last index.
        return goal == 0
