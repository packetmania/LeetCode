# Definition for a binary tree node (LeetCode 默认给出的类).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)

        return 1 + max(leftdepth, rightdepth)