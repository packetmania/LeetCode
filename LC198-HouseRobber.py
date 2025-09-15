class Solution:
    def rob(self, nums: list[int]) -> int:
        # Dynamic programming solution
        size = len(nums)
        if size < 3:
            return max(nums)

        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            # Recurrence relation: to rob house i, add its value to
            # the maximum value from all previous houses except the
            # immediate one (i-1). This ensures we follow the rule
            # of not robbing adjacent houses).
            dp[i] = max(dp[:i - 1]) + nums[i]

        return max(dp)


# 1D Dynamic Programming solution
# Time complexity: O(n^2) where n is the length of nums
#   because of the max(dp[:i - 1]) operation inside the for loop
# Space complexity: O(n)

s = Solution()
assert(s.rob([1, 2, 3, 1]) == 4)
assert(s.rob([2, 7, 9, 3, 1]) == 12)