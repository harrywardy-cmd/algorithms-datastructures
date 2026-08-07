# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Store the inorder traversal values
        result = []

        # Start the recursive inorder traversal
        self.inorder(root, result)

        # Return the completed traversal
        return result

    def inorder(self, root, result):
        # Base case: stop when we reach a null node
        if not root:
            return

        # Visit the left subtree first
        self.inorder(root.left, result)

        # Process the current node
        result.append(root.val)

        # Visit the right subtree
        self.inorder(root.right, result)
