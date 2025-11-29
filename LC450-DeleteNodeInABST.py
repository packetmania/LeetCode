# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found, perform deletion
            # Case 1: Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 2: Node with two children:
            # Find the in-order successor (smallest in the right subtree)
            temp = root.right
            while temp.left:
                temp = temp.left

            # Copy the in-order successor's value to this node
            root.val = temp.val

            # Delete the in-order successor node in the right subtree
            root.right = self.deleteNode(root.right, temp.val)

        return root

# Time Complexity: O(h) where h is the height of the tree
# Space Complexity: O(h) due to recursion stack