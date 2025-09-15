class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Solution with a variable size sliding window
        left = 0
        zeros = 0
        maxlen = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # if the count of zeros is greater than k, shrink the window
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # update the max length
            maxlen = max(maxlen, right - left + 1)

        return maxlen


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6)
assert(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10)