# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS solution
        def dfs(curr_root: TreeNode, curr_max: int) -> int:
            if curr_root is None:
                return 0

            good_nodes = 0
            if curr_root.val >= curr_max:
                good_nodes = 1
                curr_max = curr_root.val

            good_nodes += dfs(curr_root.left, curr_max)
            good_nodes += dfs(curr_root.right, curr_max)
            return good_nodes

        return dfs(root, root.val if root is not None else 0)
