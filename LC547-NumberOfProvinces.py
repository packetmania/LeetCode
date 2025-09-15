class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # DFS solution with graph
        n = len(isConnected)  # total number cities
        visited = [0 for _ in range(n)]
        provinces = 0

        def dfs(i: int):
            visited[i] = 1
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    dfs(j)
            return

        for c in range(n):
            if not visited[c]:
                provinces += 1
                dfs(c)

        return provinces


# Time complexity: O(n^2)
#   Outer loop: O(n)
#   Inner loop (DFS): O(n) per city
# Space complexity: O(n)

s = Solution()
assert(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
assert(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3)