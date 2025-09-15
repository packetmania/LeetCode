from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # Build a weighted directed graph (an adjacency list using dict)
        graph = defaultdict(list)
        for index, pair in enumerate(equations):
            graph[pair[0]].append((pair[1], values[index]))
            graph[pair[1]].append((pair[0], 1 / values[index]))

        def dfs(start: str, target: str, visited: set) -> float:
            # Base case: if we reached the target
            if start == target:
                return 1.0

            visited.add(start)  # Mark the current node as visited

            # Explore all neighbors
            for neighbor, weight in graph.get(start, []):
                if neighbor not in visited:
                    # Recursively search from neighbors
                    ret = dfs(neighbor, target, visited)
                    if ret != -1.0:
                        # Found a path, return the accumulated product
                        return weight * ret

            return -1.0  # No path found from this node

        # Process each query
        ans = []
        for query in queries:
            if query[0] not in graph or query[1] not in graph:
                ans.append(-1.0)
            elif query[0] == query[1]:
                ans.append(1.0)
            else:
                allvisited = set()
                ans.append(dfs(query[0], query[1], allvisited))

        return ans


# Time complexity: O(E + Q * (V + E)) where
#   E is the number of equations, V is the number of variables,
#   and Q is the number of queries.
# Space complexity: O(V + E) for storing the graph and the recursion
# stack in the worst case.

s = Solution()
assert(s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.0, 0.5, -1.0, 1.0, -1.0])
assert(s.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]) == [3.75, 0.4, 5.0, 0.2])
assert(s.calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]) == [0.5, 2.0, -1.0, -1.0])