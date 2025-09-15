from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        hashmap = defaultdict(int)
        count = 0
        n = len(grid)

        for r in range(n):
            hashmap[tuple(grid[r])] += 1

        # Different transpose methods:
        # transpose = [[grid[j][i] for j in range(n)] for i in range(n)]
        # transpose = list(map(list, zip(*grid)))
        transpose = [list(i) for i in zip(*grid)]

        for c in range(n):
            key = tuple(transpose[c])
            if key in hashmap:
                # find a matching (row, column) pair
                count += hashmap[key]

        return count


# Time complexity: O(n^2)
# Space complexity: O(n^2)

s = Solution()
assert(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1)
assert(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3)