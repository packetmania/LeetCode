# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        # direction: 0 for left, 1 for right
        def dfs(node, direction, length):
            if not node:
                return

            self.max_length = max(self.max_length, length)

            # If we go the same direction, reset length to 1,
            # else increment length.
            if direction == 0:
                dfs(node.left, 1, length + 1)
                dfs(node.right, 0, 1)
            else:
                dfs(node.right, 0, length + 1)
                dfs(node.left, 1, 1)

        dfs(root, 0, 0)
        dfs(root, 1, 0)

        return self.max_length