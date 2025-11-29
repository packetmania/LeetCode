# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If root is None, or root matches either p or q, return root.
        if root is None or root == p or root == q:
            return root

        # Recur for left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right calls returned non-null, this is the LCA
        if left_lca and right_lca:
            return root

        # Otherwise, return the non-null child
        return left_lca if left_lca is not None else right_lca