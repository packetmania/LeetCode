# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def dfs(root: TreeNode | None) -> list[int]:
            if not root:
                return []
            if not root.left and not root.right:  # Leaf node found
                return [root.val]

            # Recursively get leaf values from left and right subtrees
            return dfs(root.left) + dfs(root.right)

        # Get leaf value sequences for both trees
        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        # Compare the sequences
        return leaves1 == leaves2


# Time Complexity: O(N + M), where N and M are the number of nodes in the two trees.
# Space Complexity: O(H1 + H2), where H1 and H2 are the heights of the two trees (due to recursion stack).