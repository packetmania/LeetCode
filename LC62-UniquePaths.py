class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic programming solution:
        dp = [1 for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]


# 2D approach:
# dp[i][j] = dp[i-1][j] + dp[i][j-1]
#               ↑            ↑
#       previous row   current row (left)
'''
    def uniquePaths(self, m: int, n: int) -> int:
        # Dynamic programming solution:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
'''
# Optimized 1D approach:
# dp[j] = dp[j] + dp[j-1]
#            ↑       ↑
#     from above  from left
#
# We're essentially reusing the same array to represent the current row
# being calculated, overwriting the previous row's values as we go from
# left to right. This space optimization technique works for any DP where
# you only need values from the immediate previous row/column!

# Time complexity: O(m*n) where m is the number of rows and n is the number of columns.
# Space complexity: O(n) where n is the number of columns.

s = Solution()
assert(s.uniquePaths(3, 7) == 28)
assert(s.uniquePaths(3, 2) == 3)

# Combinatorial solution:
# The robot needs to make a total of (m-1) down moves and (n-1) right moves.
# The total number of unique paths is the number of ways to arrange these moves.
# This is given by the binomial coefficient C(m+n-2, m-1) or C(m+n-2, n-1).
'''
    def uniquePaths(self, m: int, n: int) -> int:
        from math import comb
        return comb(m + n - 2, m - 1)
'''