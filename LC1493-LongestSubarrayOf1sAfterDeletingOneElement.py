class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # variabe size sliding window which has maximum one zero inside
        left = 0
        zeros = 0
        maxlen = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # shrink the window if more than one 0s
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # since we must delete one even it is not 0, use right - left
            maxlen = max(maxlen, right - left)

        return maxlen


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.longestSubarray([1, 1, 0, 1]) == 3)
assert(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5)
assert(s.longestSubarray([1, 1, 1]) == 2)
