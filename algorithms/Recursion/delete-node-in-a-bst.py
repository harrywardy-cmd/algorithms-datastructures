# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: if the tree is empty, there is nothing to delete.
        if not root:
            return root

        # If the key is greater than the current node's value,
        # search for the node in the right subtree.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # If the key is smaller than the current node's value,
        # search for the node in the left subtree.
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Node to delete has been found.
        else:
            # Case 1: Node has no left child.
            # Replace it with its right child.
            if not root.left:
                return root.right

            # Case 2: Node has no right child.
            # Replace it with its left child.
            elif not root.right:
                return root.left

            # Case 3: Node has two children.
            # Find the inorder successor (smallest value in the right subtree).
            cur = root.right
            while cur.left:
                cur = cur.left

            # Replace the current node's value with the inorder successor's value.
            root.val = cur.val

            # Delete the duplicate inorder successor from the right subtree.
            root.right = self.deleteNode(root.right, root.val)

        # Return the updated subtree after deletion.
        return root
