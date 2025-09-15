from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Hint: Treat the graph as undirected. Start a dfs from the root,
        # if you come across an edge in the forward direction, you need
        # to reverse the edge.

        # Build the undirected graph
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # a -> b need reorient
            graph[b].append((a, 0))  # b -> a no need to reorient

        visited = set()
        ans = 0

        def dfs(node: int):
            nonlocal ans
            visited.add(node)
            for neighbor, flag in graph[node]:
                if neighbor not in visited:
                    ans += flag  # flag=1 means need reorienting
                    dfs(neighbor)

        dfs(0)
        return ans


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3)
assert(s.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]) == 2)