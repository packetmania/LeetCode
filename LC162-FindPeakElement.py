class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Binary search solution
        # Note that nums[i] != nums[i + 1] for all valid i,
        # so strictly there are no flat points
        low, high = 0, len(nums) - 1

        if high == 0:
            return 0

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                # If the middle element is greater than its right neighbor,
                # a peak is in the left half (including mid).
                high = mid
            else:
                # Otherwise, a peak must be in the right half.
                low = mid + 1

        return low


# Time complexity: O(log n)
# Space complexity: O(1)

s = Solution()
assert(s.findPeakElement([1,2,3,1]) == 2)
assert(s.findPeakElement([1,2,1,3,5,6,4]) == 5)