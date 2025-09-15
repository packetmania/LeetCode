class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Dynamic Programming solution
        n = len(cost)

        # Handle edge cases for very small cost arrays
        if n == 0:
            return 0
        if n == 1:
            return cost[0]

        # dp[i] will store the minimum cost to reach step i
        dp = [0] * n

        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Iterate from the third step
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # The minimum cost to reach the "top" is the minimum of reaching
        # the last step or the second-to-last step.
        return min(dp[n - 1], dp[n - 2])


# Time Complexity: O(n)
# Space Complexity: O(n)

s = Solution()
assert(s.minCostClimbingStairs([10, 15, 20]) == 15)
assert(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6)