from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # 2D BFS spreading solution
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: init the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # enqueue the rotten one
                elif grid[i][j] == 1:
                    fresh_count += 1  # count the fresh one

        minutes = 0

        # Step 2: BFS spreading, stop till no more fresh ones
        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # become rotten
                    fresh_count -= 1
                    queue.append((nr, nc, minutes+1))

        # Step 3: check the outcome and return accordingly
        return minutes if fresh_count == 0 else -1


# Time complexity: O(m * n)
# Space complexity: O(m * n)

s = Solution()
assert(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4)
assert(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1)
assert(s.orangesRotting([[0,2]]) == 0)