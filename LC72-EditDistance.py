class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Dynamic programming - 2D array
        # dp[i][j] - the minimum operations required to convert
        # the first i chars of str1 to the first j chars of str2
        size1 = len(word1)
        size2 = len(word2)

        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]

        for i in range(size1 + 1):
            dp[i][0] = i  # i chars of str1 to null str2, need i deletion
        for j in range(size2 + 1):
            dp[0][j] = j  # null str1 to j chars of str2, need j insertion

        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    # characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # characters do not match, consider all three operations
                    # 1. Replace (dp[i - 1][j - 1])
                    # 2. Delete (dp[i - 1][j])
                    # 3. Insert (dp[i][j - 1])
                    # take the minimum of the three and add 1 operation
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[size1][size2]


# Time complexity: O(m*n) where m and n are the lengths of word1 and word2
# Space complexity: O(m*n) for the dp array

s = Solution()
assert(s.minDistance("horse", "ros") == 3)
assert(s.minDistance("intention", "execution") == 5)