# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Base case:
        # If the current node is None, there is nothing to invert.
        if not root:
            return None

        # Store the left child temporarily so we don't lose it
        # when we replace it with the right child.
        temp = root.left

        # Swap the left and right children.
        root.left = root.right
        root.right = temp

        # Recursively invert the left subtree.
        self.invertTree(root.left)

        # Recursively invert the right subtree.
        self.invertTree(root.right)

        # Return the root of the inverted tree.
        return root
