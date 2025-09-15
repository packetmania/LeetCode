# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        level = 0
        maximal = float('-inf')
        queue = deque([root])

        while queue:
            size = len(queue)
            level += 1
            levelsum = 0

            for i in range(size):
                node = queue.popleft()
                levelsum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelsum > maximal:
                maximal = levelsum
                ans = level

        return ans


# Time Complexity: O(N)
# Space Complexity: O(N)

# Simple Python BFS solution implemented with deque.