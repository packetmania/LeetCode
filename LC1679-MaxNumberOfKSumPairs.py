class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # Solution with two pointers
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < k:
                left += 1
            elif curr_sum > k:
                right -= 1
            else:
                # curr_sum == k
                count += 1
                left += 1
                right -= 1

        return count


# Time complexity: O(n log n) due to sorting
# Space complexity: O(1)

s = Solution()
assert(s.maxOperations([1,2,3,4], 5) == 2)
assert(s.maxOperations([3,1,3,4,3], 6) == 1)