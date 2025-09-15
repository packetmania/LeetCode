class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Simple solution with XOR operations
        single = 0
        for i in range(len(nums)):
            single ^= nums[i]
        return single


# Simple solution with XOR operations in single for loop.
# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.singleNumber([2, 2, 1]) == 1)
assert(s.singleNumber([4, 1, 2, 1, 2]) == 4)
assert(s.singleNumber([1]) == 1)