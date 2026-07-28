# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case:
        # If we've reached an empty spot in the tree,
        # create a new node with the given value.
        if not root:
            return TreeNode(val)

        # If the value is greater than the current node,
        # recursively insert it into the right subtree.
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        # If the value is smaller than the current node,
        # recursively insert it into the left subtree.
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # Return the (possibly updated) root of the subtree.
        return root
