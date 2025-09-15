from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        # Solution with BFS on 2D maze
        m, n = len(maze), len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        maze[entrance[0]][entrance[1]] = '+'  # mark entrance visited

        while queue:
            size = len(queue)

            for i in range(size):
                (r, c, steps) = queue.popleft()

                if steps != 0 and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                    return steps  # Reach the border

                # Check neighbor cells and add not-visited empty one to the queue
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                        maze[nr][nc] = '+'  # mark visited
                        queue.append((nr, nc, steps + 1))

        return -1


# Time complexity: O(m * n)
# Space complexity: O(m * n)

s = Solution()
assert(s.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2]) == 1)
assert(s.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]],[1,0]) == 2)
assert(s.nearestExit([[".","+"]],[0,0]) == -1)