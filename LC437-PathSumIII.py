from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS with prefix-sum and dual recursions.
    #     Time complexity: O(N^2)
    #     Space complexity: O(H) where H is the height of the tree
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # DFS from the current node: count paths starting at this node
        # whose sum equals `sum_remaining`
        def dfsFromNode(node: TreeNode, sum_remaining: int) -> int:
            if node is None:
                return 0

            count = 0
            if node.val == sum_remaining:
                count += 1

            count += dfsFromNode(node.left, sum_remaining - node.val)
            count += dfsFromNode(node.right, sum_remaining - node.val)

            return count

        if root is None:
            return 0

        # Count paths that start from this root
        res = dfsFromNode(root, targetSum)

        # Plus all paths starting in the left and right subtrees
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)

        return res

    # DFS with prefix-sum and hashmap, plus backtrack.
    #     Time complexity: O(N)
    #     Space complexity: O(N)
    def pathSum_fast(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Map: prefix-sum -> how many times this prefix_sum has appeared
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # Empty path has sum 0

        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0

            # Update current prefix sum
            curr_sum += node.val

            # Number of valid paths ending at this node:
            # curr_sum - targetSum = some earlier prefix sum
            res = prefix_count[curr_sum - targetSum]

            # Record current prefix sum
            prefix_count[curr_sum] += 1

            # Continue to children
            res += dfs(node.left, curr_sum)
            res += dfs(node.right, curr_sum)

            # Backtrack: remove current prefix-sum
            prefix_count[curr_sum] -= 1

            return res

        return dfs(root, 0)
