class Solution:
    def numTilings(self, n: int) -> int:
        # Dynamic Programming with formula:
        #     dp[i] = 2 * dp[i-1] + dp[i-3]
        if n < 3:
            return n

        MOD = 10 ** 9 + 7

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]

        return dp[n] % MOD


# Time Complexity: O(n)
# Space Complexity: O(n)

s = Solution()
assert(s.numTilings(3) == 5)
assert(s.numTilings(1) == 1)