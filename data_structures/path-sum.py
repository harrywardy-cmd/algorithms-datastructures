# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # Depth First Search to explore every root-to-leaf path
        def dfs(node, currentSum):

            # If we reach a null node, this path is invalid
            if not node:
                return False

            # Add the current node's value to the running sum
            currentSum += node.val

            # If we're at a leaf node, check if the path sum matches the target
            if not node.left and not node.right and currentSum == targetSum:
                return True

            # Recursively search the left and right subtrees
            # If either subtree contains a valid path, return True
            if dfs(node.left, currentSum) or dfs(node.right, currentSum):
                return True

            # No valid path found from this node
            return False

        # Start DFS from the root with an initial sum of 0
        return dfs(root, 0)
