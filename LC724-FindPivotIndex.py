class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        answer = -1
        prefix = 0
        suffix = sum(nums[1:])

        for i in range(len(nums)):
            if prefix == suffix:
                answer = i
                break

            # If the current element is not the last one, add it to the
            # prefix sum and subtract the next one from the suffix sum.
            if i < len(nums)-1:
                prefix += nums[i]
                suffix -= nums[i+1]

        return answer


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3)
assert(s.pivotIndex([1, 2, 3]) == -1)
assert(s.pivotIndex([2, 1, -1]) == 0)