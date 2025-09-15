class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start, end = 0, k
        subsum = sum(nums[0:k])
        maxavg = subsum / k

        while end < len(nums):
            subsum -= nums[start]
            subsum += nums[end]

            if maxavg < subsum / k:
                maxavg = subsum / k

            start += 1  # slide the window
            end += 1

        return maxavg


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75000)
assert(s.findMaxAverage([5], 1) == 5.00000)
